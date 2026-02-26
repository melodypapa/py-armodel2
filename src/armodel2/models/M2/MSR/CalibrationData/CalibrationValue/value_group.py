"""ValueGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
        SwValues,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ValueGroup(ARObject):
    """AUTOSAR ValueGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label: Optional[MultilanguageLongName]
    vg_contents: Optional[SwValues]
    def __init__(self) -> None:
        """Initialize ValueGroup."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.vg_contents: Optional[SwValues] = None

    def serialize(self) -> ET.Element:
        """Serialize ValueGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ValueGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg_contents (atp_mixed - append children directly)
        if self.vg_contents is not None:
            serialized = SerializationHelper.serialize_item(self.vg_contents, "SwValues")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueGroup":
        """Deserialize XML element to ValueGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ValueGroup, cls).deserialize(element)

        # Parse label
        child = SerializationHelper.find_child_element(element, "LABEL")
        if child is not None:
            label_value = SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse vg_contents (atp_mixed - children appear directly)
        # Check if element contains expected children for SwValues
        has_mixed_children = False
        child_tags_to_check = ['V', 'VF', 'VG', 'VT', 'VTF']
        for tag in child_tags_to_check:
            if SerializationHelper.find_child_element(element, tag) is not None:
                has_mixed_children = True
                break

        if has_mixed_children:
            # Deserialize directly from current element (no wrapper)
            vg_contents_value = SerializationHelper.deserialize_by_tag(element, "SwValues")
            obj.vg_contents = vg_contents_value

        return obj



class ValueGroupBuilder(BuilderBase):
    """Builder for ValueGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ValueGroup = ValueGroup()


    def with_label(self, value: Optional[MultilanguageLongName]) -> "ValueGroupBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label = value
        return self

    def with_vg_contents(self, value: Optional[SwValues]) -> "ValueGroupBuilder":
        """Set vg_contents attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vg_contents = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> ValueGroup:
        """Build and return the ValueGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj