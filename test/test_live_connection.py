"""
Tests for thin / live-connection reports.

These PBIX files have no embedded data model — they live-connect to an external
model (an Analysis Services server or a Power BI Service dataset). Constructing
``PBIXRay`` on them raises ``LiveConnectionError`` (a ``NoEmbeddedModelError`` /
``RuntimeError`` subclass) which carries the parsed connection manifest.
"""
import os

import pytest

from pbixray import (
    PBIXRay,
    LiveConnectionError,
    NoEmbeddedModelError,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

SSAS_FILE = os.path.join(DATA_DIR, "live-connection-ssas.pbix")
PBISERVICE_FILE = os.path.join(DATA_DIR, "live-connection-pbiservice.pbix")


def test_ssas_live_raises_live_connection_error():
    with pytest.raises(LiveConnectionError) as exc_info:
        PBIXRay(SSAS_FILE)
    err = exc_info.value
    assert err.connection_type == "analysisServicesDatabaseLive"
    assert err.connections and "ConnectionString" in err.connections[0]


def test_pbiservice_live_raises_with_database_name():
    with pytest.raises(LiveConnectionError) as exc_info:
        PBIXRay(PBISERVICE_FILE)
    err = exc_info.value
    assert err.connection_type == "pbiServiceLive"
    # Power BI Service live connections expose the remote database id.
    assert err.database_name


def test_live_connection_error_is_runtime_error():
    """Backward compatibility: callers catching RuntimeError still work."""
    assert issubclass(LiveConnectionError, NoEmbeddedModelError)
    assert issubclass(NoEmbeddedModelError, RuntimeError)
    with pytest.raises(RuntimeError):
        PBIXRay(SSAS_FILE)


def test_self_contained_model_has_empty_connections(sales_returns_model):
    """Import models expose an (empty) connections list without raising."""
    assert isinstance(sales_returns_model.connections, list)
