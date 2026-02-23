"""IPv6ExtHeaderFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_i_pv6_exts: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()
        self.allowed_i_pv6_exts: list[PositiveInteger] = []

    def serialize(self) -> ET.Element:
        """Serialize IPv6ExtHeaderFilterList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPv6ExtHeaderFilterList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_i_pv6_exts (list to container "ALLOWED-I-PV6-EXTS")
        if self.allowed_i_pv6_exts:
            wrapper = ET.Element("ALLOWED-I-PV6-EXTS")
            for item in self.allowed_i_pv6_exts:
                serialized = SerializationHelper.serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-I-PV6-EXT")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterList":
        """Deserialize XML element to IPv6ExtHeaderFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPv6ExtHeaderFilterList, cls).deserialize(element)

        # Parse allowed_i_pv6_exts (list from container "ALLOWED-I-PV6-EXTS")
        obj.allowed_i_pv6_exts = []
        container = SerializationHelper.find_child_element(element, "ALLOWED-I-PV6-EXTS")
        if container is not None:
            for child in container:
                # Extract primitive value (PositiveInteger) as text
                child_value = child.text
                if child_value is not None:
                    obj.allowed_i_pv6_exts.append(child_value)

        return obj



class IPv6ExtHeaderFilterListBuilder(IdentifiableBuilder):
    """Builder for IPv6ExtHeaderFilterList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()


    def with_allowed_i_pv6_exts(self, items: list[PositiveInteger]) -> "IPv6ExtHeaderFilterListBuilder":
        """Set allowed_i_pv6_exts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts = list(items) if items else []
        return self


    def add_allowed_i_pv6_ext(self, item: PositiveInteger) -> "IPv6ExtHeaderFilterListBuilder":
        """Add a single item to allowed_i_pv6_exts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts.append(item)
        return self

    def clear_allowed_i_pv6_exts(self) -> "IPv6ExtHeaderFilterListBuilder":
        """Clear all items from allowed_i_pv6_exts list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_i_pv6_exts = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return the IPv6ExtHeaderFilterList instance with validation."""
        self._validate_instance()
        pass
        return self._obj