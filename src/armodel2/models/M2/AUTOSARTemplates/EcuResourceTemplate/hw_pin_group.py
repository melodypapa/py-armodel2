"""HwPinGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 19)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2027)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_content import (
        HwPinGroupContent,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class HwPinGroup(Identifiable):
    """AUTOSAR HwPinGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-PIN-GROUP"


    hw_pin_group_content_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-PIN-GROUP-CONTENT-REF": lambda obj, elem: setattr(obj, "hw_pin_group_content_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize HwPinGroup."""
        super().__init__()
        self.hw_pin_group_content_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPinGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPinGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_pin_group_content_ref (atp_mixed - append children directly)
        if self.hw_pin_group_content_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_pin_group_content_ref, "HwPinGroupContent")
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
    def deserialize(cls, element: ET.Element) -> "HwPinGroup":
        """Deserialize XML element to HwPinGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinGroup, cls).deserialize(element)

        # Parse hw_pin_group_content_ref (atp_mixed - children appear directly)
        # Check if element contains expected children for HwPinGroupContent
        has_mixed_children = False
        child_tags_to_check = ['HW-PIN', 'HW-PIN-GROUP']
        for tag in child_tags_to_check:
            if SerializationHelper.find_child_element(element, tag) is not None:
                has_mixed_children = True
                break

        if has_mixed_children:
            # Deserialize directly from current element (no wrapper)
            hw_pin_group_content_ref_value = SerializationHelper.deserialize_by_tag(element, "HwPinGroupContent")
            obj.hw_pin_group_content_ref = hw_pin_group_content_ref_value

        return obj



class HwPinGroupBuilder(IdentifiableBuilder):
    """Builder for HwPinGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwPinGroup = HwPinGroup()


    def with_hw_pin_group_content(self, value: Optional[HwPinGroupContent]) -> "HwPinGroupBuilder":
        """Set hw_pin_group_content attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_pin_group_content = value
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


    def build(self) -> HwPinGroup:
        """Build and return the HwPinGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj