"""EthernetCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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

    _XML_TAG = "ETHERNET-CLUSTER"


    coupling_port: Optional[TimeValue]
    mac_multicast_group_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COUPLING-PORT": lambda obj, elem: setattr(obj, "coupling_port", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MAC-MULTICAST-GROUP-REFS": lambda obj, elem: [obj.mac_multicast_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

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

        # Serialize mac_multicast_group_refs (list)
        for item in self.mac_multicast_group_refs:
            serialized = SerializationHelper.serialize_item(item, "MacMulticastGroup")
            if serialized is not None:
                wrapped = ET.Element("MAC-MULTICAST-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

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
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EthernetCluster")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(EthernetCluster, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse coupling_port
        child = SerializationHelper.find_child_element(inner_elem, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = child.text
            obj.coupling_port = coupling_port_value

        # Parse mac_multicast_group_refs (list)
        obj.mac_multicast_group_refs = []
        for child in SerializationHelper.find_all_child_elements(inner_elem, "MAC-MULTICAST-GROUP"):
            mac_multicast_group_refs_value = ARRef.deserialize(child)
            obj.mac_multicast_group_refs.append(mac_multicast_group_refs_value)

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


    def build(self) -> EthernetCluster:
        """Build and return the EthernetCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj