"""
Unit tests for XSD Parser module.
"""

import pytest
from pathlib import Path

from armodel.cfg.xsd_parser import (
    XSDParser,
    XSDElementInfo,
    XSDAttributeInfo,
    XSDComplexTypeInfo,
    XSDSimpleTypeInfo,
)


class TestXSDParser:
    """Unit tests for XSDParser class."""

    @pytest.fixture
    def xsd_file(self):
        """Get path to AUTOSAR_00046 XSD file."""
        return Path(__file__).parent.parent.parent.parent / "demos" / "xsd" / "AUTOSAR_00046" / "AUTOSAR_00046_COMPACT.xsd"

    @pytest.fixture
    def parser(self, xsd_file):
        """Get XSDParser instance for testing."""
        p = XSDParser(xsd_file)
        p.parse()
        return p

    def test_parse_initialization(self, parser):
        """Test parser initializes correctly after parsing."""
        assert parser.schema_version == "00046"
        assert parser._root is not None
        assert parser._tree is not None

    def test_complex_types_extracted(self, parser):
        """Test that complex types are extracted."""
        assert len(parser.complex_types) > 0

        # Check for known types
        assert "AUTOSAR" in parser.complex_types
        assert "AR-PACKAGE" in parser.complex_types

    def test_simple_types_extracted(self, parser):
        """Test that simple types are extracted."""
        assert len(parser.simple_types) > 0

        # Check for known types
        # Note: Type names in XSD may have different naming conventions

    def test_get_complex_type(self, parser):
        """Test getting complex type info."""
        autosar_type = parser.get_complex_type("AUTOSAR")
        assert autosar_type is not None
        assert autosar_type.name == "AUTOSAR"
        assert isinstance(autosar_type, XSDComplexTypeInfo)

    def test_get_simple_type(self, parser):
        """Test getting simple type info."""
        # Find a simple type that exists
        if parser.simple_types:
            type_name = list(parser.simple_types.keys())[0]
            simple_type = parser.get_simple_type(type_name)
            assert simple_type is not None
            assert simple_type.name == type_name
            assert isinstance(simple_type, XSDSimpleTypeInfo)

    def test_autosar_type_structure(self, parser):
        """Test AUTOSAR type has correct structure."""
        autosar_type = parser.get_complex_type("AUTOSAR")
        assert autosar_type is not None
        assert isinstance(autosar_type.elements, list)
        assert isinstance(autosar_type.attributes, list)
        assert autosar_type.base_type is None or isinstance(autosar_type.base_type, str)

    def test_ar_package_type(self, parser):
        """Test AR-PACKAGE type structure."""
        ar_package = parser.get_complex_type("AR-PACKAGE")
        assert ar_package is not None

        # Check for SHORT-NAME element
        short_name_found = False
        for elem in ar_package.elements:
            if elem.name == "SHORT-NAME":
                short_name_found = True
                assert elem.min_occurs == 1
                assert elem.max_occurs == 1
                assert elem.required is True
                break
        assert short_name_found, "SHORT-NAME element not found in AR-PACKAGE"

    def test_element_multiplicity(self, parser):
        """Test element multiplicity parsing."""
        ar_package = parser.get_complex_type("AR-PACKAGE")

        # Find an optional element (SHORT-NAME is required, look for others)
        for elem in ar_package.elements:
            if elem.min_occurs == 0:
                assert elem.required is False
                break

    def test_to_dict_structure(self, parser):
        """Test to_dict() produces correct structure."""
        result = parser.to_dict()

        assert "version" in result
        assert result["version"] == "00046"
        assert "complex_types" in result
        assert "simple_types" in result
        assert "inheritance" in result

        # Check complex types are in dict
        assert "AUTOSAR" in result["complex_types"]
        assert "AR-PACKAGE" in result["complex_types"]

    def test_to_dict_complex_type_format(self, parser):
        """Test complex type format in dict output."""
        result = parser.to_dict()
        autosar_dict = result["complex_types"]["AUTOSAR"]

        assert "base_type" in autosar_dict
        assert "abstract" in autosar_dict
        assert "elements" in autosar_dict
        assert "attributes" in autosar_dict

        # Check elements are properly formatted
        for elem in autosar_dict["elements"]:
            assert "name" in elem
            assert "type" in elem
            assert "min_occurs" in elem
            assert "max_occurs" in elem
            assert "required" in elem

    def test_get_all_elements_for_type(self, parser):
        """Test getting all elements including inherited."""
        elements = parser.get_all_elements_for_type("AUTOSAR")
        assert isinstance(elements, list)

        # If AUTOSAR has a base type, this would include inherited elements
        # For now, just verify it returns a list
        for elem in elements:
            assert isinstance(elem, XSDElementInfo)

    def test_get_all_attributes_for_type(self, parser):
        """Test getting all attributes including inherited."""
        attrs = parser.get_all_attributes_for_type("AUTOSAR")
        assert isinstance(attrs, list)

        for attr in attrs:
            assert isinstance(attr, XSDAttributeInfo)

    def test_invalid_xsd_file(self):
        """Test parser raises error for invalid file."""
        parser = XSDParser(Path("/nonexistent/file.xsd"))
        with pytest.raises(FileNotFoundError):
            parser.parse()

    def test_get_nonexistent_type(self, parser):
        """Test getting non-existent type returns None."""
        result = parser.get_complex_type("NONEXISTENT-TYPE")
        assert result is None

        result = parser.get_simple_type("NONEXISTENT-TYPE")
        assert result is None