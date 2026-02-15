import pytest
import json
from pathlib import Path

def test_create_directory_structure():
    """Test generating directory structure from package paths"""
    from tools.generate_models import create_directory_structure

    # Create temp output dir
    import tempfile
    temp_dir = Path(tempfile.mkdtemp())

    # Test with simple data
    types = [{
        "name": "TestClass",
        "type": "Class",
        "package_path": "M2::Test::SubPackage"
    }]

    # Create directory structure
    create_directory_structure(types, temp_dir)

    # Verify directories were created
    assert (temp_dir / "M2").exists()
    assert (temp_dir / "M2" / "Test").exists()
    assert (temp_dir / "M2" / "Test" / "SubPackage").exists()

    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)
