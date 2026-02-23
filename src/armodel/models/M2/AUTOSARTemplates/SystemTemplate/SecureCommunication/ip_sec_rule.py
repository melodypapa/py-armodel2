"""IPSecRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecHeaderTypeEnum,
    IPsecIpProtocolEnum,
    IPsecModeEnum,
    IPsecPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
        NetworkEndpoint,
    )



class IPSecRule(Identifiable):
    """AUTOSAR IPSecRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[Any]
    header_type: Optional[IPsecHeaderTypeEnum]
    ip_protocol: Optional[IPsecIpProtocolEnum]
    local_certificate_refs: list[Any]
    local_id: Optional[String]
    local_port_range: Optional[PositiveInteger]
    mode: Optional[IPsecModeEnum]
    policy: Optional[IPsecPolicyEnum]
    pre_shared_key_ref: Optional[ARRef]
    priority: Optional[PositiveInteger]
    remote_refs: list[Any]
    remote_id: Optional[String]
    remote_ip_refs: list[ARRef]
    remote_port: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IPSecRule."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.header_type: Optional[IPsecHeaderTypeEnum] = None
        self.ip_protocol: Optional[IPsecIpProtocolEnum] = None
        self.local_certificate_refs: list[Any] = []
        self.local_id: Optional[String] = None
        self.local_port_range: Optional[PositiveInteger] = None
        self.mode: Optional[IPsecModeEnum] = None
        self.policy: Optional[IPsecPolicyEnum] = None
        self.pre_shared_key_ref: Optional[ARRef] = None
        self.priority: Optional[PositiveInteger] = None
        self.remote_refs: list[Any] = []
        self.remote_id: Optional[String] = None
        self.remote_ip_refs: list[ARRef] = []
        self.remote_port: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IPSecRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPSecRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = SerializationHelper.serialize_item(self.direction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_type
        if self.header_type is not None:
            serialized = SerializationHelper.serialize_item(self.header_type, "IPsecHeaderTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_protocol
        if self.ip_protocol is not None:
            serialized = SerializationHelper.serialize_item(self.ip_protocol, "IPsecIpProtocolEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-PROTOCOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_certificate_refs (list to container "LOCAL-CERTIFICATE-REFS")
        if self.local_certificate_refs:
            wrapper = ET.Element("LOCAL-CERTIFICATE-REFS")
            for item in self.local_certificate_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("LOCAL-CERTIFICATE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize local_id
        if self.local_id is not None:
            serialized = SerializationHelper.serialize_item(self.local_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_port_range
        if self.local_port_range is not None:
            serialized = SerializationHelper.serialize_item(self.local_port_range, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-PORT-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode
        if self.mode is not None:
            serialized = SerializationHelper.serialize_item(self.mode, "IPsecModeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize policy
        if self.policy is not None:
            serialized = SerializationHelper.serialize_item(self.policy, "IPsecPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pre_shared_key_ref
        if self.pre_shared_key_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pre_shared_key_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRE-SHARED-KEY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_refs (list to container "REMOTE-REFS")
        if self.remote_refs:
            wrapper = ET.Element("REMOTE-REFS")
            for item in self.remote_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize remote_id
        if self.remote_id is not None:
            serialized = SerializationHelper.serialize_item(self.remote_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_ip_refs (list to container "REMOTE-IP-REFS")
        if self.remote_ip_refs:
            wrapper = ET.Element("REMOTE-IP-REFS")
            for item in self.remote_ip_refs:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-IP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize remote_port
        if self.remote_port is not None:
            serialized = SerializationHelper.serialize_item(self.remote_port, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecRule":
        """Deserialize XML element to IPSecRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPSecRule, cls).deserialize(element)

        # Parse direction
        child = SerializationHelper.find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = child.text
            obj.direction = direction_value

        # Parse header_type
        child = SerializationHelper.find_child_element(element, "HEADER-TYPE")
        if child is not None:
            header_type_value = IPsecHeaderTypeEnum.deserialize(child)
            obj.header_type = header_type_value

        # Parse ip_protocol
        child = SerializationHelper.find_child_element(element, "IP-PROTOCOL")
        if child is not None:
            ip_protocol_value = IPsecIpProtocolEnum.deserialize(child)
            obj.ip_protocol = ip_protocol_value

        # Parse local_certificate_refs (list from container "LOCAL-CERTIFICATE-REFS")
        obj.local_certificate_refs = []
        container = SerializationHelper.find_child_element(element, "LOCAL-CERTIFICATE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.local_certificate_refs.append(child_value)

        # Parse local_id
        child = SerializationHelper.find_child_element(element, "LOCAL-ID")
        if child is not None:
            local_id_value = child.text
            obj.local_id = local_id_value

        # Parse local_port_range
        child = SerializationHelper.find_child_element(element, "LOCAL-PORT-RANGE")
        if child is not None:
            local_port_range_value = child.text
            obj.local_port_range = local_port_range_value

        # Parse mode
        child = SerializationHelper.find_child_element(element, "MODE")
        if child is not None:
            mode_value = IPsecModeEnum.deserialize(child)
            obj.mode = mode_value

        # Parse policy
        child = SerializationHelper.find_child_element(element, "POLICY")
        if child is not None:
            policy_value = IPsecPolicyEnum.deserialize(child)
            obj.policy = policy_value

        # Parse pre_shared_key_ref
        child = SerializationHelper.find_child_element(element, "PRE-SHARED-KEY-REF")
        if child is not None:
            pre_shared_key_ref_value = ARRef.deserialize(child)
            obj.pre_shared_key_ref = pre_shared_key_ref_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse remote_refs (list from container "REMOTE-REFS")
        obj.remote_refs = []
        container = SerializationHelper.find_child_element(element, "REMOTE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_refs.append(child_value)

        # Parse remote_id
        child = SerializationHelper.find_child_element(element, "REMOTE-ID")
        if child is not None:
            remote_id_value = child.text
            obj.remote_id = remote_id_value

        # Parse remote_ip_refs (list from container "REMOTE-IP-REFS")
        obj.remote_ip_refs = []
        container = SerializationHelper.find_child_element(element, "REMOTE-IP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_ip_refs.append(child_value)

        # Parse remote_port
        child = SerializationHelper.find_child_element(element, "REMOTE-PORT")
        if child is not None:
            remote_port_value = child.text
            obj.remote_port = remote_port_value

        return obj



class IPSecRuleBuilder(IdentifiableBuilder):
    """Builder for IPSecRule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPSecRule = IPSecRule()


    def with_direction(self, value: Optional[any (Communication)]) -> "IPSecRuleBuilder":
        """Set direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direction = value
        return self

    def with_header_type(self, value: Optional[IPsecHeaderTypeEnum]) -> "IPSecRuleBuilder":
        """Set header_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_type = value
        return self

    def with_ip_protocol(self, value: Optional[IPsecIpProtocolEnum]) -> "IPSecRuleBuilder":
        """Set ip_protocol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_protocol = value
        return self

    def with_local_certificates(self, items: list[any (CryptoService)]) -> "IPSecRuleBuilder":
        """Set local_certificates list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.local_certificates = list(items) if items else []
        return self

    def with_local_id(self, value: Optional[String]) -> "IPSecRuleBuilder":
        """Set local_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_id = value
        return self

    def with_local_port_range(self, value: Optional[PositiveInteger]) -> "IPSecRuleBuilder":
        """Set local_port_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_port_range = value
        return self

    def with_mode(self, value: Optional[IPsecModeEnum]) -> "IPSecRuleBuilder":
        """Set mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode = value
        return self

    def with_policy(self, value: Optional[IPsecPolicyEnum]) -> "IPSecRuleBuilder":
        """Set policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.policy = value
        return self

    def with_pre_shared_key(self, value: Optional[CryptoServiceKey]) -> "IPSecRuleBuilder":
        """Set pre_shared_key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pre_shared_key = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "IPSecRuleBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_remotes(self, items: list[any (CryptoService)]) -> "IPSecRuleBuilder":
        """Set remotes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remotes = list(items) if items else []
        return self

    def with_remote_id(self, value: Optional[String]) -> "IPSecRuleBuilder":
        """Set remote_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remote_id = value
        return self

    def with_remote_ips(self, items: list[NetworkEndpoint]) -> "IPSecRuleBuilder":
        """Set remote_ips list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remote_ips = list(items) if items else []
        return self

    def with_remote_port(self, value: Optional[PositiveInteger]) -> "IPSecRuleBuilder":
        """Set remote_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remote_port = value
        return self


    def add_local_certificate(self, item: any (CryptoService)) -> "IPSecRuleBuilder":
        """Add a single item to local_certificates list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.local_certificates.append(item)
        return self

    def clear_local_certificates(self) -> "IPSecRuleBuilder":
        """Clear all items from local_certificates list.

        Returns:
            self for method chaining
        """
        self._obj.local_certificates = []
        return self

    def add_remote(self, item: any (CryptoService)) -> "IPSecRuleBuilder":
        """Add a single item to remotes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remotes.append(item)
        return self

    def clear_remotes(self) -> "IPSecRuleBuilder":
        """Clear all items from remotes list.

        Returns:
            self for method chaining
        """
        self._obj.remotes = []
        return self

    def add_remote_ip(self, item: NetworkEndpoint) -> "IPSecRuleBuilder":
        """Add a single item to remote_ips list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remote_ips.append(item)
        return self

    def clear_remote_ips(self) -> "IPSecRuleBuilder":
        """Clear all items from remote_ips list.

        Returns:
            self for method chaining
        """
        self._obj.remote_ips = []
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


    def build(self) -> IPSecRule:
        """Build and return the IPSecRule instance with validation."""
        self._validate_instance()
        pass
        return self._obj