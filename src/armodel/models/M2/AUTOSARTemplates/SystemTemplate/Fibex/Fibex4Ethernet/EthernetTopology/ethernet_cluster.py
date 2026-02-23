"""EthernetCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class EthernetCluster(ARObject):
    """AUTOSAR EthernetCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupling_port: Optional[TimeValue]
    mac_multicast_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EthernetCluster."""
        super().__init__()
        self.coupling_port: Optional[TimeValue] = None
        self.mac_multicast_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EthernetCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize coupling_port
        if self.coupling_port is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_port, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("COUPLING-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUP-REFS")
        if self.mac_multicast_group_refs:
            container = ET.Element("MAC-MULTICAST-GROUP-REFS")
            for item in self.mac_multicast_group_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("MacMulticastGroup", package_data):
                    # Simple primitive type
                    child = ET.Element("MAC-MULTICAST-GROUP")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("MacMulticastGroup", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EthernetCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCluster":
        """Deserialize XML element to EthernetCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetCluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EthernetCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse coupling_port
        child = SerializationHelper.find_child_element(inner_elem, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = child.text
            obj.coupling_port = coupling_port_value

        # Parse mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUP-REFS")
        obj.mac_multicast_group_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "MAC-MULTICAST-GROUP-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("MacMulticastGroup", package_data):
                    child_value = child.text
                elif is_enum_type("MacMulticastGroup", package_data):
                    child_value = MacMulticastGroup.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mac_multicast_group_refs.append(child_value)

        return obj



class EthernetClusterBuilder(BuilderBase):
    """Builder for EthernetCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetCluster = EthernetCluster()


    def with_coupling_port(self, value: Optional[TimeValue]) -> "EthernetClusterBuilder":
        """Set coupling_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coupling_port = value
        return self

    def with_mac_multicast_groups(self, items: list[MacMulticastGroup]) -> "EthernetClusterBuilder":
        """Set mac_multicast_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups = list(items) if items else []
        return self


    def add_mac_multicast_group(self, item: MacMulticastGroup) -> "EthernetClusterBuilder":
        """Add a single item to mac_multicast_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups.append(item)
        return self

    def clear_mac_multicast_groups(self) -> "EthernetClusterBuilder":
        """Clear all items from mac_multicast_groups list.

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups = []
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


    def build(self) -> EthernetCluster:
        """Build and return the EthernetCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj