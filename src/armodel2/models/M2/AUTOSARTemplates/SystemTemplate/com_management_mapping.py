"""ComManagementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 282)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ComManagementMapping(Identifiable):
    """AUTOSAR ComManagementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COM-MANAGEMENT-MAPPING"


    com_refs: list[ARRef]
    physical_channel_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COM-REFS": lambda obj, elem: [obj.com_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "PHYSICAL-CHANNEL-REFS": ("_POLYMORPHIC_LIST", "physical_channel_refs", ["CanPhysicalChannel", "TtcanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel"]),
    }


    def __init__(self) -> None:
        """Initialize ComManagementMapping."""
        super().__init__()
        self.com_refs: list[ARRef] = []
        self.physical_channel_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ComManagementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComManagementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize com_refs (list to container "COM-REFS")
        if self.com_refs:
            wrapper = ET.Element("COM-REFS")
            for item in self.com_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("COM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
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
    def deserialize(cls, element: ET.Element) -> "ComManagementMapping":
        """Deserialize XML element to ComManagementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComManagementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComManagementMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COM-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.com_refs.append(ARRef.deserialize(item_elem))
            elif tag == "PHYSICAL-CHANNEL-REFS":
                for item_elem in child:
                    obj.physical_channel_refs.append(ARRef.deserialize(item_elem))

        return obj



class ComManagementMappingBuilder(IdentifiableBuilder):
    """Builder for ComManagementMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ComManagementMapping = ComManagementMapping()


    def with_coms(self, items: list[PortGroup]) -> "ComManagementMappingBuilder":
        """Set coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coms = list(items) if items else []
        return self

    def with_physical_channels(self, items: list[PhysicalChannel]) -> "ComManagementMappingBuilder":
        """Set physical_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = list(items) if items else []
        return self


    def add_com(self, item: PortGroup) -> "ComManagementMappingBuilder":
        """Add a single item to coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coms.append(item)
        return self

    def clear_coms(self) -> "ComManagementMappingBuilder":
        """Clear all items from coms list.

        Returns:
            self for method chaining
        """
        self._obj.coms = []
        return self

    def add_physical_channel(self, item: PhysicalChannel) -> "ComManagementMappingBuilder":
        """Add a single item to physical_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physical_channels.append(item)
        return self

    def clear_physical_channels(self) -> "ComManagementMappingBuilder":
        """Clear all items from physical_channels list.

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = []
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


    def build(self) -> ComManagementMapping:
        """Build and return the ComManagementMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj