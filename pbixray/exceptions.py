"""Exception hierarchy for pbixray.

``NoEmbeddedModelError`` (and its subclass ``LiveConnectionError``) also inherit
from :class:`RuntimeError` so that callers written against the previous
``RuntimeError`` contract keep working.
"""


class PBIXRayError(Exception):
    """Base class for all pbixray errors."""


class NoEmbeddedModelError(PBIXRayError, RuntimeError):
    """Raised when a PBIX/XLSX file contains no embedded data model to parse.

    This is the generic case: there is no ``DataModel`` (PBIX) or
    ``xl/model/item.data`` (XLSX) entry, and no connection manifest explaining
    why. See :class:`LiveConnectionError` for thin/live-connection reports.
    """


class LiveConnectionError(NoEmbeddedModelError):
    """Raised when a file is a thin report bound to an *external* model.

    Power BI reports that live-connect to an Analysis Services server
    (``analysisServicesDatabaseLive``) or a Power BI Service dataset
    (``pbiServiceLive``) store no model on disk — the model lives on the remote
    server, so there is nothing to extract.

    The parsed ``Connections`` entries are exposed on :attr:`connections`, with
    the first connection's most useful fields available as convenience
    attributes.
    """

    def __init__(self, connections):
        self.connections = list(connections) if connections else []
        first = self.connections[0] if self.connections else {}
        self.connection_type = first.get("ConnectionType")
        self.connection_string = first.get("ConnectionString")
        # Present for Power BI Service live connections.
        self.database_name = first.get("PbiModelDatabaseName")
        super().__init__(
            "No embedded data model: this is a live-connection report "
            f"(ConnectionType={self.connection_type!r}). The model lives in an "
            "external source; inspect the exception's .connections for details."
        )
