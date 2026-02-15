import pytest
import json
from pathlib import Path
import sys

def test_parse_mapping_json():
    """Test parsing mapping.json file"""
    # Add parent directory to path so we can import tools
    sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
    from generate_models import parse_mapping_json

    # Create test mapping.json
    test_data = {
        "types": [
            {
                "name": "TestClass",
                "type": "Class",
                "package_path": "M2::Test"
            }
        ]
    }

    test_file = Path("test_mapping.json")
    test_file.write_text(json.dumps(test_data))

    # Parse
    result = parse_mapping_json(test_file)

    # Verify
    assert len(result["types"]) == 1
    assert result["types"][0]["name"] == "TestClass"

    # Cleanup
    test_file.unlink()

    # Cleanup
    test_file.unlink()
