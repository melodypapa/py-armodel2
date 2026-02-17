import pytest
import json
from pathlib import Path

def test_parse_mapping_json():
    """Test parsing mapping.json file"""
    from tools.generate_models import parse_mapping_json

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

    import tempfile
    test_file = Path(tempfile.mktemp(suffix=".json"))
    test_file.write_text(json.dumps(test_data))

    result = parse_mapping_json(test_file)
    assert len(result["types"]) == 1
    assert result["types"][0]["name"] == "TestClass"

    # Cleanup
    test_file.unlink()

def test_generate_class_code():
    """Test generating Python class code"""
    from tools.generate_models import generate_class_code

    type_def = {
        "name": "TestInterface",
        "type": "Class",
        "package_path": "M2::Test"
    }

    hierarchy_info = {
        "TestInterface": {
            "parent": None,
            "is_abstract": False
        }
    }

    package_data = {
        "M2::Test": {
            "attributes": []
        }
    }

    code = generate_class_code(type_def, hierarchy_info, package_data)

    # Check that class is generated
    assert "class TestInterface(ARObject):" in code
    assert "def __init__(self)" in code
    # Check that it inherits from ARObject (which has serialize/deserialize)
    assert "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject" in code

def test_generate_builder_code():
    """Test generating builder class code"""
    from tools.generate_models import generate_builder_code

    type_def = {
        "name": "TestInterface",
        "type": "Class",
        "package_path": "M2::Test"
    }

    code = generate_builder_code(type_def)

    # Check that builder is generated
    assert "class TestInterfaceBuilder:" in code
    assert "def __init__(self)" in code
    assert "def build(self)" in code

def test_full_generation(tmp_path):
    """Test full code generation process"""
    from tools.generate_models import generate_all_models

    # Create test mapping
    test_data = {
        "types": [
            {
                "name": "TestClass",
                "type": "Class",
                "package_path": "M2::TestPackage"
            }
        ]
    }

    # Create test hierarchy
    hierarchy_data = """## Class Hierarchy
* TestClass
"""

    import tempfile
    mapping_file = Path(tempfile.mktemp(suffix=".json"))
    mapping_file.write_text(json.dumps(test_data))

    hierarchy_file = Path(tempfile.mktemp(suffix=".json"))
    hierarchy_file.write_text(hierarchy_data)

    output_dir = tmp_path / "output"

    generate_all_models(mapping_file, hierarchy_file, output_dir)

    # Check files were created
    assert (output_dir / "M2" / "TestPackage" / "test_class.py").exists()
    assert (output_dir / "M2" / "__init__.py").exists()

    # Check file content
    content = (output_dir / "M2" / "TestPackage" / "test_class.py").read_text()
    assert "class TestClass(ARObject):" in content
    assert "class TestClassBuilder:" in content
