"""IPSecRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecHeaderTypeEnum,
    IPsecIpProtocolEnum,
    IPsecModeEnum,
    IPsecPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
        NetworkEndpoint,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class IPSecRule(Identifiable):
    """AUTOSAR IPSecRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-P-SEC-RULE"


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
    _DESERIALIZE_DISPATCH = {
        "DIRECTION": lambda obj, elem: setattr(obj, "direction", SerializationHelper.deserialize_by_tag(elem, "any (Communication)")),
        "HEADER-TYPE": lambda obj, elem: setattr(obj, "header_type", IPsecHeaderTypeEnum.deserialize(elem)),
        "IP-PROTOCOL": lambda obj, elem: setattr(obj, "ip_protocol", IPsecIpProtocolEnum.deserialize(elem)),
        "LOCAL-CERTIFICATE-REFS": lambda obj, elem: [obj.local_certificate_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "LOCAL-ID": lambda obj, elem: setattr(obj, "local_id", SerializationHelper.deserialize_by_tag(elem, "String")),
        "LOCAL-PORT-RANGE": lambda obj, elem: setattr(obj, "local_port_range", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MODE": lambda obj, elem: setattr(obj, "mode", IPsecModeEnum.deserialize(elem)),
        "POLICY": lambda obj, elem: setattr(obj, "policy", IPsecPolicyEnum.deserialize(elem)),
        "PRE-SHARED-KEY-REF": lambda obj, elem: setattr(obj, "pre_shared_key_ref", ARRef.deserialize(elem)),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REMOTE-REFS": lambda obj, elem: [obj.remote_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REMOTE-ID": lambda obj, elem: setattr(obj, "remote_id", SerializationHelper.deserialize_by_tag(elem, "String")),
        "REMOTE-IP-REFS": lambda obj, elem: [obj.remote_ip_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REMOTE-PORT": lambda obj, elem: setattr(obj, "remote_port", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIRECTION":
                setattr(obj, "direction", SerializationHelper.deserialize_by_tag(child, "any (Communication)"))
            elif tag == "HEADER-TYPE":
                setattr(obj, "header_type", IPsecHeaderTypeEnum.deserialize(child))
            elif tag == "IP-PROTOCOL":
                setattr(obj, "ip_protocol", IPsecIpProtocolEnum.deserialize(child))
            elif tag == "LOCAL-CERTIFICATE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.local_certificate_refs.append(ARRef.deserialize(item_elem))
            elif tag == "LOCAL-ID":
                setattr(obj, "local_id", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "LOCAL-PORT-RANGE":
                setattr(obj, "local_port_range", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MODE":
                setattr(obj, "mode", IPsecModeEnum.deserialize(child))
            elif tag == "POLICY":
                setattr(obj, "policy", IPsecPolicyEnum.deserialize(child))
            elif tag == "PRE-SHARED-KEY-REF":
                setattr(obj, "pre_shared_key_ref", ARRef.deserialize(child))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REMOTE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.remote_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REMOTE-ID":
                setattr(obj, "remote_id", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "REMOTE-IP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.remote_ip_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REMOTE-PORT":
                setattr(obj, "remote_port", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IPSecRuleBuilder(IdentifiableBuilder):
    """Builder for IPSecRule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPSecRule = IPSecRule()


    def with_direction(self, value: Optional[Any]) -> "IPSecRuleBuilder":
        """Set direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'direction' is required and cannot be None")
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
            raise ValueError("Attribute 'header_type' is required and cannot be None")
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
            raise ValueError("Attribute 'ip_protocol' is required and cannot be None")
        self._obj.ip_protocol = value
        return self

    def with_local_certificates(self, items: list[Any]) -> "IPSecRuleBuilder":
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
            raise ValueError("Attribute 'local_id' is required and cannot be None")
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
            raise ValueError("Attribute 'local_port_range' is required and cannot be None")
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
            raise ValueError("Attribute 'mode' is required and cannot be None")
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
            raise ValueError("Attribute 'policy' is required and cannot be None")
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
            raise ValueError("Attribute 'pre_shared_key' is required and cannot be None")
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
            raise ValueError("Attribute 'priority' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_remotes(self, items: list[Any]) -> "IPSecRuleBuilder":
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
            raise ValueError("Attribute 'remote_id' is required and cannot be None")
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
            raise ValueError("Attribute 'remote_port' is required and cannot be None")
        self._obj.remote_port = value
        return self


    def add_local_certificate(self, item: Any) -> "IPSecRuleBuilder":
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

    def add_remote(self, item: Any) -> "IPSecRuleBuilder":
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "direction",
        "headerType",
        "ipProtocol",
        "localCertificate",
        "localId",
        "localPortRange",
        "mode",
        "policy",
        "preSharedKey",
        "priority",
        "remote",
        "remoteId",
        "remoteIp",
        "remotePort",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPSecRule:
        """Build and return the IPSecRule instance with validation."""
        self._validate_instance()
        return self._obj