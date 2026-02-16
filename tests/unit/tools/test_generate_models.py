import pytest
import json
from pathlib import Path

from tools.generate_models import create_directory_structure


class TestGenerateModels:
    """Unit tests for generate_models module."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        import tempfile
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_types = [{
            "name": "TestClass",
            "type": "Class",
            "package_path": "M2::Test::SubPackage"
        }]

    def teardown_method(self):
        """Cleanup test fixtures."""
        import shutil
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def test_create_directory_structure(self):
        """Test generating directory structure from package paths."""
        # Create directory structure
        package_data = {
            "M2::Test::SubPackage": {
                "attributes": []
            }
        }
        create_directory_structure(self.test_types, self.temp_dir, package_data)

        # Verify directories were created
        assert (self.temp_dir / "M2").exists()
        assert (self.temp_dir / "M2" / "Test").exists()
        assert (self.temp_dir / "M2" / "Test" / "SubPackage").exists()
