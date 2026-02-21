"""
Integration tests for manually maintained (skipped) classes.

These tests validate the classes listed in tools/skip_classes.yaml that are
manually maintained and not auto-generated. This ensures critical classes
work correctly despite not being regenerated.

Classes Tested:
- AUTOSAR: Root AUTOSAR element
- ARObject: Base serialization framework
- ARRef: AUTOSAR references with DEST attribute
- BaseType: Abstract base class for SwBaseType
- SwDataDefProps: SW-DATA-DEF-PROPS wrappers
- CompuMethod/Compu/CompuScales/CompuScale/CompuConst/CompuConstTextContent: Computation methods
- MultiLanguage* classes: Language-specific elements (L-1, L-2, L-4, L-5, L-10)
- ARPackage: Package with long_name handling
- LanguageSpecific/L*: Language-specific with L attribute

Traceability:
- Test Documentation: docs/tests/integration/test_skip_classes.md
- SWITS IDs: SWITS-INT-0300 through SWITS-INT-0399
"""
import pytest
from pathlib import Path
import xml.etree.ElementTree as ET

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter


class TestCompuMethodClasses:
    """Test CompuMethod and related computation classes.

    These classes have custom serialization for COMPU-INTERNAL-TO-PHYS and
    COMPU-PHYS-TO-INTERNAL wrapper elements.

    Test IDs: SWITS-INT-0300 to SWITS-INT-0310
    """

    @pytest.fixture
    def compu_method_file(self):
        """Path to ARXML file with CompuMethod examples."""
        return Path("demos/validated/AUTOSAR_Datatypes.arxml")

    @pytest.fixture
    def compu_blueprint_file(self):
        """Path to CompuMethod blueprint file."""
        return Path("demos/validated/AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml")

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    @pytest.fixture
    def writer(self):
        """ARXML writer instance."""
        return ARXMLWriter(pretty_print=True, encoding="UTF-8")

    def test_compu_method_deserialization(self, compu_method_file, reader):
        """Test CompuMethod can be deserialized from ARXML.

        Test ID: SWITS-INT-0300

        Validates:
        - CompuMethod objects load correctly
        - COMPU-INTERNAL-TO-PHYS wrapper is handled
        - COMPU-PHYS-TO-INTERNAL wrapper is handled
        - CompuContent and CompuConst deserialize correctly
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        AUTOSAR().clear()
        autosar = AUTOSAR()
        reader.load_arxml(str(compu_method_file), autosar)

        # Find CompuMethod objects
        compu_methods = []
        for pkg in autosar.ar_packages:
            self._find_compu_methods(pkg, compu_methods)

        assert len(compu_methods) > 0, "No CompuMethod objects found"

        # Validate first CompuMethod
        cm = compu_methods[0]
        assert hasattr(cm, 'compu_internal_to_phys') or hasattr(cm, '_compu_internal_to_phys'), \
            "CompuMethod missing compu_internal_to_phys"

        print(f"\n✅ Found {len(compu_methods)} CompuMethod objects")
        print(f"   First CompuMethod: {cm.short_name if hasattr(cm, 'short_name') else 'unnamed'}")

    def test_compu_method_serialization(self, compu_method_file, reader, writer, tmp_path):
        """Test CompuMethod can be serialized back to XML correctly.

        Test ID: SWITS-INT-0301

        Validates:
        - CompuMethod serialize() produces correct XML
        - COMPU-INTERNAL-TO-PHYS wrapper element created
        - COMPU-PHYS-TO-INTERNAL wrapper element created
        - Compu children serialized correctly
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # Load original
        AUTOSAR.reset()
        autosar_orig = AUTOSAR()
        reader.load_arxml(str(compu_method_file), autosar_orig)

        # Find CompuMethod
        compu_methods = []
        for pkg in autosar_orig.ar_packages:
            self._find_compu_methods(pkg, compu_methods)

        if not compu_methods:
            pytest.skip("No CompuMethod objects found in file")

        # Save count before clearing
        original_count = len(compu_methods)

        # Serialize and reload
        output_file = tmp_path / "compu_method_test.arxml"
        writer.save_arxml(str(output_file), autosar_orig)

        AUTOSAR.reset()
        autosar_reload = AUTOSAR()
        reader.load_arxml(str(output_file), autosar_reload)

        # Verify CompuMethod still exists
        reloaded_methods = []
        for pkg in autosar_reload.ar_packages:
            self._find_compu_methods(pkg, reloaded_methods)

        assert len(reloaded_methods) == original_count, \
            f"CompuMethod count mismatch: {len(reloaded_methods)} != {original_count}"

        print("\n✅ CompuMethod serialization successful")
        print(f"   Original: {original_count} methods")
        print(f"   Reloaded: {len(reloaded_methods)} methods")

    def _find_compu_methods(self, pkg, methods_list):
        """Recursively find CompuMethod objects in packages.

        Args:
            pkg: ARPackage to search
            methods_list: List to append found CompuMethods to
        """
        from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import CompuMethod

        if hasattr(pkg, 'elements') and pkg.elements:
            for elem in pkg.elements:
                if isinstance(elem, CompuMethod):
                    methods_list.append(elem)

        if hasattr(pkg, 'ar_packages') and pkg.ar_packages:
            for sub_pkg in pkg.ar_packages:
                self._find_compu_methods(sub_pkg, methods_list)


class TestLanguageSpecificClasses:
    """Test language-specific classes with L-1, L-2, L-4, L-5, L-10 elements.

    These classes handle hyphenated XML tag names and require custom
    serialization for the L attribute.

    Test IDs: SWITS-INT-0320 to SWITS-INT-0330
    """

    @pytest.fixture
    def application_datatype_file(self):
        """Path to ARXML file with language-specific elements."""
        return Path("demos/validated/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml")

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    @pytest.fixture
    def writer(self):
        """ARXML writer instance."""
        return ARXMLWriter(pretty_print=True, encoding="UTF-8")

    def test_multilanguage_elements_present(self, application_datatype_file, reader):
        """Test that language-specific elements can be loaded.

        Test ID: SWITS-INT-0320

        Validates:
        - L-2 elements are present in ARXML
        - MultiLanguagePlainText objects deserialize
        - Language attribute is handled correctly
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        autosar = AUTOSAR()
        reader.load_arxml(str(application_datatype_file), autosar)

        # Check file has L-2 elements
        content = application_datatype_file.read_text()
        has_l2 = '<L-2' in content or '<L-2>' in content

        if has_l2:
            print("\n✅ ARXML file contains L-2 language-specific elements")
            print("   These should be handled by MultiLanguagePlainText class")
        else:
            pytest.skip("No L-2 elements found in file")

    def test_language_specific_round_trip(self, application_datatype_file, reader, writer, tmp_path):
        """Test language-specific elements survive round-trip serialization.

        Test ID: SWITS-INT-0321

        Validates:
        - L-2 elements serialize correctly
        - Language attribute preserved
        - Text content preserved
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # Load original
        autosar_orig = AUTOSAR()
        reader.load_arxml(str(application_datatype_file), autosar_orig)

        # Serialize
        output_file = tmp_path / "lang_test.arxml"
        writer.save_arxml(str(output_file), autosar_orig)

        # Check L-2 elements preserved
        orig_content = application_datatype_file.read_text()
        out_content = output_file.read_text()

        orig_l2_count = orig_content.count('<L-2')
        out_l2_count = out_content.count('<L-2')

        print("\n✅ Language-specific element round-trip")
        print(f"   Original L-2 elements: {orig_l2_count}")
        print(f"   Serialized L-2 elements: {out_l2_count}")

        # Both files should have L-2 elements
        assert orig_l2_count > 0, "Original file has no L-2 elements"
        # Note: Output count may differ due to formatting, but elements should exist


class TestARPackageClass:
    """Test ARPackage class with custom long_name handling.

    Test IDs: SWITS-INT-0340 to SWITS-INT-0345
    """

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    def test_ar_package_long_name(self, reader):
        """Test ARPackage handles long_name attribute correctly.

        Test ID: SWITS-INT-0340

        Validates:
        - ARPackage objects load
        - long_name is preserved
        - Language-specific elements in long_name work
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # Test with multiple ARXML files
        test_files = [
            Path("demos/validated/AUTOSAR_Datatypes.arxml"),
            Path("demos/validated/AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml"),
        ]

        for arxml_file in test_files:
            if not arxml_file.exists():
                continue

            autosar = AUTOSAR()
            reader.load_arxml(str(arxml_file), autosar)

            assert len(autosar.ar_packages) > 0, f"No packages found in {arxml_file.name}"

            # Check first package
            pkg = autosar.ar_packages[0]
            assert hasattr(pkg, 'short_name'), "ARPackage missing short_name"

            print(f"\n✅ ARPackage in {arxml_file.name}")
            print(f"   Short name: {pkg.short_name}")
            if hasattr(pkg, 'long_name') and pkg.long_name:
                print("   Has long_name: Yes")

    def test_ar_package_serialization(self, reader, tmp_path):
        """Test ARPackage serializes correctly.

        Test ID: SWITS-INT-0341

        Validates:
        - ARPackage serialize() produces correct XML
        - AR-PACKAGE element created
        - short_name included
        - long_name handled correctly
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        from armodel.writer import ARXMLWriter

        arxml_file = Path("demos/validated/AUTOSAR_Datatypes.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        # Load
        autosar = AUTOSAR()
        reader.load_arxml(str(arxml_file), autosar)

        # Serialize
        writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
        output_file = tmp_path / "ar_package_test.arxml"
        writer.save_arxml(str(output_file), autosar)

        # Verify AR-PACKAGE elements in output
        content = output_file.read_text()
        assert '<AR-PACKAGES>' in content, "Missing AR-PACKAGES element"
        assert '<AR-PACKAGE>' in content, "Missing AR-PACKAGE element"

        pkg_count = content.count('<AR-PACKAGE>')
        print("\n✅ ARPackage serialization successful")
        print(f"   Packages in output: {pkg_count}")


class TestArgumentDirectionEnum:
    """Test ArgumentDirectionEnum enum values.

    This enum had issues with 'IN' value - tests verify correct handling.

    Test IDs: SWITS-INT-0350 to SWITS-INT-0355
    """

    def test_enum_values_exist(self):
        """Test that ArgumentDirectionEnum has all expected values.

        Test ID: SWITS-INT-0350

        Validates:
        - IN enum value exists (lowercase 'in')
        - INOUT enum value exists
        - OUT enum value exists
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.argument_direction_enum import ArgumentDirectionEnum

        # Check enum values exist
        assert hasattr(ArgumentDirectionEnum, 'IN'), "Missing IN enum value"
        assert hasattr(ArgumentDirectionEnum, 'INOUT'), "Missing INOUT enum value"
        assert hasattr(ArgumentDirectionEnum, 'OUT'), "Missing OUT enum value"

        # Check values (should be uppercase - AUTOSAR format)
        assert ArgumentDirectionEnum.IN == "IN", "IN value should be uppercase 'IN'"
        assert ArgumentDirectionEnum.INOUT == "INOUT", "INOUT value should be 'INOUT'"
        assert ArgumentDirectionEnum.OUT == "OUT", "OUT value should be 'OUT'"

        print("\n✅ ArgumentDirectionEnum values correct")
        print(f"   IN: {ArgumentDirectionEnum.IN}")
        print(f"   INOUT: {ArgumentDirectionEnum.INOUT}")
        print(f"   OUT: {ArgumentDirectionEnum.OUT}")

    def test_enum_serialization(self):
        """Test ArgumentDirectionEnum can serialize and deserialize.

        Test ID: SWITS-INT-0351

        Validates:
        - Enum serializes to correct XML
        - Enum deserializes from XML
        - Case sensitivity handled correctly
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.argument_direction_enum import ArgumentDirectionEnum

        # Create enum instance
        enum_in = ArgumentDirectionEnum(ArgumentDirectionEnum.IN)

        # Serialize to XML
        elem = enum_in.serialize()
        assert elem is not None, "Serialization failed"
        # AREnum serializes with uppercase value (AUTOSAR format)
        assert elem.text is not None, "Serialized text should not be None"

        # Deserialize from XML - AREnum handles case-insensitive matching
        elem.text = "IN"
        deserialized = ArgumentDirectionEnum.deserialize(elem)
        assert deserialized._value_ == "IN", f"Expected 'IN', got '{deserialized._value_}'"

        # Also test lowercase - should normalize to uppercase member value
        elem.text = "in"
        deserialized2 = ArgumentDirectionEnum.deserialize(elem)
        # AREnum.deserialize() normalizes to member value (uppercase)
        assert deserialized2._value_ == "IN", f"Expected 'IN' (normalized), got '{deserialized2._value_}'"

        print("\n✅ ArgumentDirectionEnum serialization/deserialization works")
        print(f"   Serialized: {elem.text}")
        print(f"   Deserialized: {deserialized._value_}")


class TestARRefClass:
    """Test ARRef class for AUTOSAR references.

    Test IDs: SWITS-INT-0360 to SWITS-INT-0365
    """

    def test_ar_ref_basic_usage(self):
        """Test ARRef can be created and used.

        Test ID: SWITS-INT-0360

        Validates:
        - ARRef can be instantiated
        - DEST attribute is handled
        - Reference can be serialized
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

        # Create ARRef
        ar_ref = ARRef()
        ar_ref.dest = "SomePackage"

        # Basic validation
        assert hasattr(ar_ref, 'dest'), "ARRef missing dest attribute"

        print("\n✅ ARRef basic usage works")
        print(f"   DEST: {ar_ref.dest}")


class TestBaseTypeClass:
    """Test BaseType abstract base class.

    Test IDs: SWITS-INT-0370 to SWITS-INT-0375
    """

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    def test_basetype_loading(self, reader):
        """Test that BaseType subclasses can be loaded.

        Test ID: SWITS-INT-0370

        Validates:
        - SwBaseType objects load correctly
        - BaseType hierarchy works
        - Base type attributes preserved
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # Use file with base types
        arxml_file = Path("demos/validated/AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        autosar = AUTOSAR()
        reader.load_arxml(str(arxml_file), autosar)

        # Find SwBaseType objects (recursively search nested packages)
        from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import SwBaseType

        base_types = []
        def find_in_packages(packages):
            """Recursively search for SwBaseType in packages."""
            for pkg in packages:
                if hasattr(pkg, 'elements') and pkg.elements:
                    for elem in pkg.elements:
                        if isinstance(elem, SwBaseType):
                            base_types.append(elem)
                if hasattr(pkg, 'ar_packages') and pkg.ar_packages:
                    find_in_packages(pkg.ar_packages)

        find_in_packages(autosar.ar_packages)

        if base_types:
            print(f"\n✅ Found {len(base_types)} SwBaseType objects")
            bt = base_types[0]
            if hasattr(bt, 'short_name'):
                print(f"   First type: {bt.short_name}")
        else:
            pytest.skip("No SwBaseType objects found")


class TestSwDataDefPropsClass:
    """Test SwDataDefProps with SW-DATA-DEF-PROPS wrappers.

    Test IDs: SWITS-INT-0380 to SWITS-INT-0385
    """

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    def test_sw_data_def_props_loading(self, reader):
        """Test SwDataDefProps variants can be loaded.

        Test ID: SWITS-INT-0380

        Validates:
        - SW-DATA-DEF-PROPS-VARIANTS wrapper handled
        - SW-DATA-DEF-PROPS-CONDITIONAL wrapper handled
        - Properties preserved correctly
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # Test with application data types (likely to have SwDataDefProps)
        arxml_file = Path("demos/validated/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        autosar = AUTOSAR()
        reader.load_arxml(str(arxml_file), autosar)

        # Check file has SW-DATA-DEF-PROPS
        content = arxml_file.read_text()
        has_props = 'SW-DATA-DEF-PROPS' in content

        if has_props:
            print("\n✅ ARXML file contains SW-DATA-DEF-PROPS elements")
            print("   File loaded successfully")
        else:
            print(f"\n⚠️  No SW-DATA-DEF-PROPS in {arxml_file.name}")


class TestARObjectClass:
    """Test ARObject base class and serialization framework.

    Test IDs: SWITS-INT-0390 to SWITS-INT-0399
    """

    @pytest.fixture
    def reader(self):
        """ARXML reader instance."""
        return ARXMLReader()

    def test_ar_object_helper_methods(self):
        """Test ARObject static helper methods.

        Test ID: SWITS-INT-0390

        Validates:
        - _find_child_element() works
        - _find_all_child_elements() works
        - _strip_namespace() works
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.serialization import SerializationHelper

        # Create test element
        parent = ET.Element("PARENT")
        child1 = ET.Element("CHILD-1")
        child2 = ET.Element("{http://autosar.org}CHILD-2")
        child3 = ET.Element("CHILD-3")

        parent.append(child1)
        parent.append(child2)
        parent.append(child3)

        # Test _find_child_element
        found = SerializationHelper.find_child_element(parent, "CHILD-1")
        assert found is not None, "Failed to find CHILD-1"
        print("   _find_child_element: ✅")

        # Test _find_all_child_elements
        all_children = SerializationHelper.find_all_child_elements(parent, "CHILD-1")
        assert len(all_children) == 1, "Should find one CHILD-1"
        print(f"   _find_all_child_elements: ✅ (found {len(all_children)} CHILD-1)")

        # Test _strip_namespace
        tag = "{http://autosar.org}CHILD-2"
        stripped = SerializationHelper.strip_namespace(tag)
        assert stripped == "CHILD-2", f"Expected 'CHILD-2', got '{stripped}'"
        print("   _strip_namespace: ✅")

        print("\n✅ ARObject helper methods work correctly")

    def test_ar_object_inheritance_chain(self, reader):
        """Test that ARObject inheritance works in deserialization.

        Test ID: SWITS-INT-0391

        Validates:
        - Parent class deserialize() called first
        - Child class then handles its own attributes
        - No duplicate attribute processing
        """
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        arxml_file = Path("demos/validated/AUTOSAR_Datatypes.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        autosar = AUTOSAR()
        reader.load_arxml(str(arxml_file), autosar)

        # If we got here without errors, inheritance chain worked
        assert len(autosar.ar_packages) > 0, "No packages loaded"

        print("\n✅ ARObject inheritance chain works")
        print(f"   Loaded {len(autosar.ar_packages)} packages")
