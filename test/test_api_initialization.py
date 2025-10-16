"""
Test suite for PBIXRay initialization and basic functionality.
Tests both PBIX and XLSX file support.
"""
import pytest
from pathlib import Path
from pbixray import PBIXRay


class TestInitialization:
    """Test PBIXRay initialization with different file types."""

    def test_pbix_initialization(self, primary_pbix_file):
        """Test successful initialization with a PBIX file."""
        model = PBIXRay(str(primary_pbix_file))
        assert model is not None
        assert hasattr(model, '_metadata_handler')
        assert hasattr(model, '_vertipaq_decoder')

    def test_xlsx_initialization(self, primary_xlsx_file):
        """Test successful initialization with an XLSX file."""
        model = PBIXRay(str(primary_xlsx_file))
        assert model is not None
        assert hasattr(model, '_metadata_handler')
        assert hasattr(model, '_vertipaq_decoder')

    @pytest.mark.parametrize("file_fixture", ["primary_pbix_file", "primary_xlsx_file"])
    def test_initialization_with_both_types(self, file_fixture, request):
        """Test initialization works with both PBIX and XLSX files."""
        file_path = request.getfixturevalue(file_fixture)
        model = PBIXRay(str(file_path))
        assert model is not None

    def test_initialization_with_invalid_file(self, tmp_path):
        """Test that initialization fails gracefully with invalid file."""
        invalid_file = tmp_path / "invalid.pbix"
        invalid_file.write_text("not a valid pbix file")
        
        with pytest.raises(Exception):  # Should raise some kind of error
            PBIXRay(str(invalid_file))

    def test_initialization_with_nonexistent_file(self):
        """Test that initialization fails with nonexistent file."""
        with pytest.raises(FileNotFoundError):
            PBIXRay("/nonexistent/path/to/file.pbix")


class TestFileTypeDetection:
    """Test that the library correctly detects file types."""

    def test_pbix_file_type_detected(self, pbix_model):
        """Verify PBIX file is detected as pbix type."""
        # Access internal data model to check file type
        assert pbix_model._metadata_handler._data_model.file_type == "pbix"

    def test_xlsx_file_type_detected(self, xlsx_model):
        """Verify XLSX file is detected as xlsx type."""
        # Access internal data model to check file type
        assert xlsx_model._metadata_handler._data_model.file_type == "xlsx"


class TestMultipleFiles:
    """Test handling of multiple files."""

    def test_multiple_pbix_files_can_be_loaded(self, sample_pbix_files):
        """Test that multiple PBIX files can be loaded sequentially."""
        models = []
        for file_path in sample_pbix_files[:3]:  # Test first 3 files
            model = PBIXRay(str(file_path))
            models.append(model)
            assert model is not None
        
        assert len(models) > 0

    def test_multiple_xlsx_files_can_be_loaded(self, sample_xlsx_files):
        """Test that multiple XLSX files can be loaded sequentially."""
        models = []
        for file_path in sample_xlsx_files[:3]:  # Test first 3 files
            model = PBIXRay(str(file_path))
            models.append(model)
            assert model is not None
        
        assert len(models) > 0
