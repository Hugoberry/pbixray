"""
Pytest configuration and shared fixtures for PBIXRay tests.
"""
import pytest
from pathlib import Path
import sys
import os

# Add the pbixray package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pbixray import PBIXRay


# Define test data paths
DATA_DIR = Path(__file__).parent.parent / "data"


@pytest.fixture(scope="session")
def sample_pbix_files():
    """Return list of available PBIX test files."""
    pbix_files = list(DATA_DIR.glob("*.pbix"))
    if not pbix_files:
        pytest.skip("No PBIX files found in data directory")
    return pbix_files


@pytest.fixture(scope="session")
def sample_xlsx_files():
    """Return list of available XLSX test files with Power Pivot."""
    xlsx_files = list(DATA_DIR.glob("*.xlsx"))
    if not xlsx_files:
        pytest.skip("No XLSX files found in data directory")
    return xlsx_files


@pytest.fixture(scope="session")
def primary_pbix_file(sample_pbix_files):
    """Return the primary PBIX file for detailed testing."""
    # Prefer "Sales & Returns Sample" if available
    for file in sample_pbix_files:
        if "Sales" in file.name and "Returns" in file.name:
            return file
    # Otherwise return the first file
    return sample_pbix_files[0]


@pytest.fixture(scope="session")
def primary_xlsx_file(sample_xlsx_files):
    """Return the primary XLSX file for detailed testing."""
    # Prefer "Supplier Quality Analysis" if available
    for file in sample_xlsx_files:
        if "Supplier" in file.name and "Quality" in file.name:
            return file
    # Otherwise return the first file
    return sample_xlsx_files[0]


@pytest.fixture(scope="module")
def pbix_model(primary_pbix_file):
    """Create a PBIXRay instance for the primary PBIX file."""
    return PBIXRay(str(primary_pbix_file))


@pytest.fixture(scope="module")
def xlsx_model(primary_xlsx_file):
    """Create a PBIXRay instance for the primary XLSX file."""
    return PBIXRay(str(primary_xlsx_file))


@pytest.fixture(scope="session")
def rls_pbix_file(sample_pbix_files):
    """Return PBIX file with RLS if available."""
    for file in sample_pbix_files:
        if "rls" in file.name.lower():
            return file
    return None


@pytest.fixture(scope="module")
def rls_model(rls_pbix_file):
    """Create a PBIXRay instance for RLS testing."""
    if rls_pbix_file is None:
        pytest.skip("No RLS sample file available")
    return PBIXRay(str(rls_pbix_file))
