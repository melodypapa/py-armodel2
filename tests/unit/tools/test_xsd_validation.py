"""Unit tests for XSD validation tool."""

import json

from tools.validation.comparator import SchemaComparator
from tools.validation.json_loader import JSONClassLoader
from tools.validation.models import (
    DiscrepancySeverity,
    DiscrepancyType,
    JSONClass,
    JSONMember,
    XSDComplexType,
    XSDMember,
)
from tools.validation.xsd_parser import XSDParser


class TestXSDParser:
    """Tests for XSD parser."""

    def test_xsd_to_multiplicity_0_to_1(self):
        """Test multiplicity conversion for 0..1."""
        parser = XSDParser.__new__(XSDParser)
        result = parser._xsd_to_multiplicity(0, "1")
        assert result == "0..1"

    def test_xsd_to_multiplicity_1_to_1(self):
        """Test multiplicity conversion for 1..1."""
        parser = XSDParser.__new__(XSDParser)
        result = parser._xsd_to_multiplicity(1, "1")
        assert result == "1"

    def test_xsd_to_multiplicity_0_to_unbounded(self):
        """Test multiplicity conversion for *."""
        parser = XSDParser.__new__(XSDParser)
        result = parser._xsd_to_multiplicity(0, "unbounded")
        assert result == "*"

    def test_xsd_to_multiplicity_0_to_negative_1(self):
        """Test multiplicity conversion for -1 (unbounded)."""
        parser = XSDParser.__new__(XSDParser)
        result = parser._xsd_to_multiplicity(0, "-1")
        assert result == "*"

    def test_detect_reference_type_refs(self):
        """Test reference type detection for REFS pattern."""
        parser = XSDParser.__new__(XSDParser)

        # Create mock element
        from lxml import etree

        elem = etree.Element("element", name="ELEMENT-REFS")

        is_ref, ref_kind = parser._detect_reference_type("ELEMENT-REFS", elem)
        assert is_ref is True
        assert ref_kind == "ref"

    def test_detect_reference_type_irefs(self):
        """Test reference type detection for IREFS pattern."""
        parser = XSDParser.__new__(XSDParser)

        from lxml import etree

        elem = etree.Element("element", name="COLLECTED-INSTANCE-IREFS")

        is_ref, ref_kind = parser._detect_reference_type("COLLECTED-INSTANCE-IREFS", elem)
        assert is_ref is True
        assert ref_kind == "iref"

    def test_detect_reference_type_trefs(self):
        """Test reference type detection for TREFS pattern."""
        parser = XSDParser.__new__(XSDParser)

        from lxml import etree

        elem = etree.Element("element", name="TYPE-DEF-TREFS")

        is_ref, ref_kind = parser._detect_reference_type("TYPE-DEF-TREFS", elem)
        assert is_ref is True
        assert ref_kind == "tref"

    def test_detect_reference_type_none(self):
        """Test reference type detection for non-reference."""
        parser = XSDParser.__new__(XSDParser)

        from lxml import etree

        elem = etree.Element("element", name="AUTO-COLLECT")

        is_ref, ref_kind = parser._detect_reference_type("AUTO-COLLECT", elem)
        assert is_ref is False
        assert ref_kind is None


class TestJSONClassLoader:
    """Tests for JSON class loader."""

    def test_load_all_classes(self, tmp_path):
        """Test loading all classes from JSON files."""
        # Create temporary JSON file
        json_dir = tmp_path / "packages"
        json_dir.mkdir()

        test_data = {
            "package": "Test::Package",
            "classes": [
                {
                    "name": "TestClass",
                    "package": "Test::Package",
                    "is_abstract": False,
                    "atp_type": None,
                    "parent": None,
                    "bases": [],
                    "children": [],
                    "subclasses": [],
                    "attributes": {
                        "testAttr": {
                            "type": "TestType",
                            "multiplicity": "0..1",
                            "kind": "attribute",
                            "is_ref": False,
                            "note": "Test attribute",
                        }
                    },
                }
            ],
        }

        test_file = json_dir / "test.classes.json"
        with open(test_file, "w") as f:
            json.dump(test_data, f)

        # Load classes
        loader = JSONClassLoader(str(json_dir))
        classes = loader.load_all()

        assert "TestClass" in classes
        assert classes["TestClass"].name == "TestClass"
        assert "testAttr" in classes["TestClass"].attributes
        assert classes["TestClass"].attributes["testAttr"].type == "TestType"


class TestSchemaComparator:
    """Tests for schema comparator."""

    def test_compare_all_no_discrepancies(self):
        """Test comparison with matching schemas."""
        # Create matching JSON and XSD definitions
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={
                    "testAttr": JSONMember(
                        type="TestType",
                        multiplicity="0..1",
                        kind="attribute",
                        is_ref=False,
                    )
                },
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={
                    "testAttr": XSDMember(
                        xsd_name="TEST-ATTR",
                        qualified_name="TestClass.testAttr",
                        json_name="testAttr",
                        type_name="TestType",
                        min_occurs=0,
                        max_occurs="1",
                        multiplicity="0..1",
                        is_reference=False,
                        reference_kind=None,
                        is_attribute=False,
                    )
                },
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 0

    def test_compare_missing_member(self):
        """Test detection of missing member in JSON."""
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={},  # Empty attributes
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={
                    "testAttr": XSDMember(
                        xsd_name="TEST-ATTR",
                        qualified_name="TestClass.testAttr",
                        json_name="testAttr",
                        type_name="TestType",
                        min_occurs=1,
                        max_occurs="1",
                        multiplicity="1",
                        is_reference=False,
                        reference_kind=None,
                        is_attribute=False,
                    )
                },
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 1
        assert discrepancies[0].discrepancy_type == DiscrepancyType.MISSING_MEMBER
        assert discrepancies[0].severity == DiscrepancySeverity.ERROR

    def test_compare_extra_member(self):
        """Test detection of extra member in JSON."""
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={
                    "extraAttr": JSONMember(
                        type="ExtraType",
                        multiplicity="1",
                        kind="attribute",
                        is_ref=False,
                    )
                },
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={},  # Empty members
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 1
        assert discrepancies[0].discrepancy_type == DiscrepancyType.EXTRA_MEMBER

    def test_compare_type_mismatch(self):
        """Test detection of type mismatch."""
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={
                    "testAttr": JSONMember(
                        type="TestType1",
                        multiplicity="0..1",
                        kind="attribute",
                        is_ref=False,
                    )
                },
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={
                    "testAttr": XSDMember(
                        xsd_name="TEST-ATTR",
                        qualified_name="TestClass.testAttr",
                        json_name="testAttr",
                        type_name="TestType2",  # Different type
                        min_occurs=0,
                        max_occurs="1",
                        multiplicity="0..1",
                        is_reference=False,
                        reference_kind=None,
                        is_attribute=False,
                    )
                },
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 1
        assert discrepancies[0].discrepancy_type == DiscrepancyType.TYPE_MISMATCH

    def test_compare_multiplicity_mismatch(self):
        """Test detection of multiplicity mismatch."""
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={
                    "testAttr": JSONMember(
                        type="TestType",
                        multiplicity="0..1",  # Optional
                        kind="attribute",
                        is_ref=False,
                    )
                },
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={
                    "testAttr": XSDMember(
                        xsd_name="TEST-ATTR",
                        qualified_name="TestClass.testAttr",
                        json_name="testAttr",
                        type_name="TestType",
                        min_occurs=1,
                        max_occurs="1",
                        multiplicity="1",  # Required
                        is_reference=False,
                        reference_kind=None,
                        is_attribute=False,
                    )
                },
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 1
        assert discrepancies[0].discrepancy_type == DiscrepancyType.MULTIPLICITY_MISMATCH

    def test_compare_ref_kind_mismatch(self):
        """Test detection of reference kind mismatch."""
        json_classes = {
            "TestClass": JSONClass(
                name="TestClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={
                    "testAttr": JSONMember(
                        type="TestType",
                        multiplicity="0..1",
                        kind="attribute",
                        is_ref=False,  # Not a reference
                    )
                },
            )
        }

        xsd_types = {
            "TestClass": XSDComplexType(
                xsd_name="TEST-CLASS",
                qualified_name="TestClass",
                members={
                    "testAttr": XSDMember(
                        xsd_name="TEST-REFS",
                        qualified_name="TestClass.testAttr",
                        json_name="testAttr",
                        type_name="TestType",
                        min_occurs=0,
                        max_occurs="1",
                        multiplicity="0..1",
                        is_reference=True,  # Is a reference
                        reference_kind="ref",
                        is_attribute=False,
                    )
                },
                base_types=[],
            )
        }

        comparator = SchemaComparator()
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        assert len(discrepancies) == 1
        assert discrepancies[0].discrepancy_type == DiscrepancyType.REF_KIND_MISMATCH

    def test_normalize_type_ar_prefix(self):
        """Test type normalization with AR: prefix."""
        comparator = SchemaComparator.__new__(SchemaComparator)
        result = comparator._normalize_type("AR:TestType")
        assert result == "TestType"

    def test_normalize_type_subtypes_enum(self):
        """Test type normalization with --SUBTYPES-ENUM suffix."""
        comparator = SchemaComparator.__new__(SchemaComparator)
        result = comparator._normalize_type("TestType--SUBTYPES-ENUM")
        assert result == "TestType"

    def test_normalize_type_simple(self):
        """Test type normalization with --SIMPLE suffix."""
        comparator = SchemaComparator.__new__(SchemaComparator)
        result = comparator._normalize_type("TestType--SIMPLE")
        assert result == "TestType"

    def test_normalize_type_enum(self):
        """Test type normalization with -ENUM suffix."""
        comparator = SchemaComparator.__new__(SchemaComparator)
        result = comparator._normalize_type("TestType-ENUM")
        assert result == "TestType"

    def test_normalize_type_combined(self):
        """Test type normalization with both prefix and suffix."""
        comparator = SchemaComparator.__new__(SchemaComparator)
        result = comparator._normalize_type("AR:TestType--SUBTYPES-ENUM")
        assert result == "TestType"

    def test_skip_classes(self):
        """Test that skipped classes are not compared."""
        json_classes = {
            "SkippedClass": JSONClass(
                name="SkippedClass",
                package="Test::Package",
                is_abstract=False,
                atp_type=None,
                parent=None,
                bases=[],
                children=[],
                subclasses=[],
                attributes={},
            )
        }

        xsd_types = {}  # Empty - class doesn't exist in XSD

        comparator = SchemaComparator(skip_classes={"SkippedClass"})
        discrepancies = comparator.compare_all(json_classes, xsd_types)

        # Should not report missing_xsd_type for skipped class
        assert len(discrepancies) == 0


class TestReporter:
    """Tests for discrepancy reporter."""

    def test_get_summary_empty(self):
        """Test summary with no discrepancies."""
        from tools.validation.reporter import DiscrepancyReporter

        reporter = DiscrepancyReporter([])
        summary = reporter._get_summary()

        assert summary["total"] == 0
        assert summary[DiscrepancySeverity.ERROR.value] == 0
        assert summary[DiscrepancySeverity.WARNING.value] == 0
        assert summary[DiscrepancySeverity.INFO.value] == 0

    def test_get_summary_with_discrepancies(self):
        """Test summary with discrepancies."""
        from tools.validation.reporter import DiscrepancyReporter
        from tools.validation.models import Discrepancy

        discrepancies = [
            Discrepancy(
                discrepancy_type=DiscrepancyType.MISSING_MEMBER,
                severity=DiscrepancySeverity.ERROR,
                class_name="TestClass",
                member_name="testAttr",
                message="Test error",
            ),
            Discrepancy(
                discrepancy_type=DiscrepancyType.TYPE_MISMATCH,
                severity=DiscrepancySeverity.WARNING,
                class_name="TestClass",
                member_name="testAttr",
                message="Test warning",
            ),
            Discrepancy(
                discrepancy_type=DiscrepancyType.EXTRA_MEMBER,
                severity=DiscrepancySeverity.INFO,
                class_name="TestClass",
                member_name="testAttr",
                message="Test info",
            ),
        ]

        reporter = DiscrepancyReporter(discrepancies)
        summary = reporter._get_summary()

        assert summary["total"] == 3
        assert summary[DiscrepancySeverity.ERROR.value] == 1
        assert summary[DiscrepancySeverity.WARNING.value] == 1
        assert summary[DiscrepancySeverity.INFO.value] == 1

    def test_filter_by_severity(self):
        """Test filtering by severity level."""
        from tools.validation.reporter import DiscrepancyReporter
        from tools.validation.models import Discrepancy

        discrepancies = [
            Discrepancy(
                discrepancy_type=DiscrepancyType.MISSING_MEMBER,
                severity=DiscrepancySeverity.ERROR,
                class_name="TestClass",
                member_name="testAttr",
                message="Test error",
            ),
            Discrepancy(
                discrepancy_type=DiscrepancyType.TYPE_MISMATCH,
                severity=DiscrepancySeverity.WARNING,
                class_name="TestClass",
                member_name="testAttr",
                message="Test warning",
            ),
            Discrepancy(
                discrepancy_type=DiscrepancyType.EXTRA_MEMBER,
                severity=DiscrepancySeverity.INFO,
                class_name="TestClass",
                member_name="testAttr",
                message="Test info",
            ),
        ]

        reporter = DiscrepancyReporter(discrepancies)

        # Filter by WARNING (should include ERROR and WARNING)
        filtered = reporter._filter_by_severity(DiscrepancySeverity.WARNING)
        assert len(filtered) == 2

        # Filter by ERROR (should include only ERROR)
        filtered = reporter._filter_by_severity(DiscrepancySeverity.ERROR)
        assert len(filtered) == 1

        # Filter by INFO (should include all)
        filtered = reporter._filter_by_severity(DiscrepancySeverity.INFO)
        assert len(filtered) == 3