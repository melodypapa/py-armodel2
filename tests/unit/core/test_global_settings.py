import pytest
import warnings
import xml.etree.ElementTree as ET

from armodel.core import GlobalSettingsManager


class TestGlobalSettingsManager:
    """Unit tests for GlobalSettingsManager class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures - reset settings before each test."""
        self.settings = GlobalSettingsManager()
        self.settings.reset()

    def test_singleton_pattern(self):
        """Test that GlobalSettingsManager follows singleton pattern."""
        settings1 = GlobalSettingsManager()
        settings2 = GlobalSettingsManager()
        assert settings1 is settings2

    def test_default_values(self):
        """Test default settings values."""
        assert self.settings.strict_validation is False
        assert self.settings.warn_on_unrecognized is True

    def test_set_and_get(self):
        """Test setting and getting values."""
        self.settings.set("strict_validation", True)
        assert self.settings.get("strict_validation") is True

        self.settings.set("custom_key", "custom_value")
        assert self.settings.get("custom_key") == "custom_value"

    def test_property_setters(self):
        """Test property setters."""
        self.settings.strict_validation = True
        assert self.settings.strict_validation is True

        self.settings.warn_on_unrecognized = False
        assert self.settings.warn_on_unrecognized is False

    def test_reset(self):
        """Test reset restores default values."""
        self.settings.strict_validation = True
        self.settings.warn_on_unrecognized = False

        self.settings.reset()

        assert self.settings.strict_validation is False
        assert self.settings.warn_on_unrecognized is True

    def test_get_with_default(self):
        """Test get with default value for unknown key."""
        value = self.settings.get("unknown_key", "default_value")
        assert value == "default_value"


class TestGlobalSettingsValidation:
    """Tests for validation behavior using GlobalSettingsManager."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Reset settings before and after each test."""
        self.settings = GlobalSettingsManager()
        self.settings.reset()
        yield
        self.settings.reset()

    def test_warn_on_unrecognized_elements(self):
        """Test warn_on_unrecognized emits warning for unrecognized elements."""
        import xml.etree.ElementTree as ET
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.serialization import SerializationHelper

        # Create a simple test class with custom deserialize
        class TestClass(ARObject):
            test_attr: str = None

            def __init__(self):
                super().__init__()
                self.test_attr: str = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize with validation."""
                obj = super().deserialize(element)

                # Parse test_attr
                child = SerializationHelper.find_child_element(element, "TEST-ATTR")
                if child is not None and child.text:
                    obj.test_attr = child.text

                # Check for unrecognized elements (warn_on_unrecognized is enabled by default)
                for child in element:
                    tag = SerializationHelper.strip_namespace(child.tag)
                    if tag not in ["TEST-ATTR"]:
                        if self.settings.warn_on_unrecognized:
                            import warnings
                            warnings.warn(f"Unrecognized XML element: <{tag}>")

                return obj

        xml_str = '''<TEST-CLASS>
            <TEST-ATTR>value</TEST-ATTR>
            <UNRECOGNIZED-ELEMENT>ignored</UNRECOGNIZED-ELEMENT>
        </TEST-CLASS>'''
        element = ET.fromstring(xml_str)

        # Capture warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            TestClass.deserialize(element)

            # Should have warning about unrecognized element
            unrecognized_warnings = [
                warning for warning in w
                if "Unrecognized XML element" in str(warning.message)
            ]
            assert len(unrecognized_warnings) == 1
            assert "<UNRECOGNIZED-ELEMENT>" in str(unrecognized_warnings[0].message)

    def test_strict_validation_raises_error(self):
        """Test strict_validation raises ValueError for unrecognized elements."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.serialization import SerializationHelper

        # Create a simple test class with custom deserialize
        class TestClass(ARObject):
            test_attr: str = None

            def __init__(self):
                super().__init__()
                self.test_attr: str = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize with validation."""
                obj = super().deserialize(element)

                # Parse test_attr
                child = SerializationHelper.find_child_element(element, "TEST-ATTR")
                if child is not None and child.text:
                    obj.test_attr = child.text

                # Check for unrecognized elements (strict validation)
                for child in element:
                    tag = SerializationHelper.strip_namespace(child.tag)
                    if tag not in ["TEST-ATTR"]:
                        if self.settings.strict_validation:
                            raise ValueError(f"Unrecognized XML element: <{tag}>")

                return obj

        xml_str = '''<TEST-CLASS>
            <TEST-ATTR>value</TEST-ATTR>
            <UNRECOGNIZED-ELEMENT>ignored</UNRECOGNIZED-ELEMENT>
        </TEST-CLASS>'''
        element = ET.fromstring(xml_str)

        # Enable strict validation
        self.settings.strict_validation = True

        # Should raise ValueError
        with pytest.raises(ValueError, match="Unrecognized XML element"):
            TestClass.deserialize(element)

    def test_no_warning_when_disabled(self):
        """Test no warning when warn_on_unrecognized is False."""
        import xml.etree.ElementTree as ET
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.serialization import SerializationHelper

        # Create a simple test class with custom deserialize
        class TestClass(ARObject):
            test_attr: str = None

            def __init__(self):
                super().__init__()
                self.test_attr: str = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize with validation."""
                obj = super().deserialize(element)

                # Parse test_attr
                child = SerializationHelper.find_child_element(element, "TEST-ATTR")
                if child is not None and child.text:
                    obj.test_attr = child.text

                # Check for unrecognized elements (warn_on_unrecognized is disabled)
                for child in element:
                    tag = SerializationHelper.strip_namespace(child.tag)
                    if tag not in ["TEST-ATTR"]:
                        if self.settings.warn_on_unrecognized:
                            import warnings
                            warnings.warn(f"Unrecognized XML element: <{tag}>")

                return obj

        xml_str = '''<TEST-CLASS>
            <TEST-ATTR>value</TEST-ATTR>
            <UNRECOGNIZED-ELEMENT>ignored</UNRECOGNIZED-ELEMENT>
        </TEST-CLASS>'''
        element = ET.fromstring(xml_str)

        # Disable warning
        self.settings.warn_on_unrecognized = False

        # Capture warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            TestClass.deserialize(element)

            # Should NOT have warning
            unrecognized_warnings = [
                warning for warning in w
                if "Unrecognized XML element" in str(warning.message)
            ]
            assert len(unrecognized_warnings) == 0
