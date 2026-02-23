"""VlanMembership AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanMembership(ARObject):
    """AUTOSAR VlanMembership."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_priority: Optional[PositiveInteger]
    dhcp_address: Optional[Any]
    send_activity: Optional[Any]
    vlan_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize VlanMembership."""
        super().__init__()
        self.default_priority: Optional[PositiveInteger] = None
        self.dhcp_address: Optional[Any] = None
        self.send_activity: Optional[Any] = None
        self.vlan_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize VlanMembership to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VlanMembership, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_priority
        if self.default_priority is not None:
            serialized = SerializationHelper.serialize_item(self.default_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dhcp_address
        if self.dhcp_address is not None:
            serialized = SerializationHelper.serialize_item(self.dhcp_address, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DHCP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize send_activity
        if self.send_activity is not None:
            serialized = SerializationHelper.serialize_item(self.send_activity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEND-ACTIVITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_ref
        if self.vlan_ref is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VlanMembership":
        """Deserialize XML element to VlanMembership object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VlanMembership object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VlanMembership, cls).deserialize(element)

        # Parse default_priority
        child = SerializationHelper.find_child_element(element, "DEFAULT-PRIORITY")
        if child is not None:
            default_priority_value = child.text
            obj.default_priority = default_priority_value

        # Parse dhcp_address
        child = SerializationHelper.find_child_element(element, "DHCP-ADDRESS")
        if child is not None:
            dhcp_address_value = child.text
            obj.dhcp_address = dhcp_address_value

        # Parse send_activity
        child = SerializationHelper.find_child_element(element, "SEND-ACTIVITY")
        if child is not None:
            send_activity_value = child.text
            obj.send_activity = send_activity_value

        # Parse vlan_ref
        child = SerializationHelper.find_child_element(element, "VLAN-REF")
        if child is not None:
            vlan_ref_value = ARRef.deserialize(child)
            obj.vlan_ref = vlan_ref_value

        return obj



class VlanMembershipBuilder(BuilderBase):
    """Builder for VlanMembership with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VlanMembership = VlanMembership()


    def with_default_priority(self, value: Optional[PositiveInteger]) -> "VlanMembershipBuilder":
        """Set default_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_priority = value
        return self

    def with_dhcp_address(self, value: Optional[any (DhcpServer)]) -> "VlanMembershipBuilder":
        """Set dhcp_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dhcp_address = value
        return self

    def with_send_activity(self, value: Optional[any (EthernetSwitchVlan)]) -> "VlanMembershipBuilder":
        """Set send_activity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.send_activity = value
        return self

    def with_vlan(self, value: Optional[any (EthernetPhysical)]) -> "VlanMembershipBuilder":
        """Set vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan = value
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


    def build(self) -> VlanMembership:
        """Build and return the VlanMembership instance with validation."""
        self._validate_instance()
        pass
        return self._obj