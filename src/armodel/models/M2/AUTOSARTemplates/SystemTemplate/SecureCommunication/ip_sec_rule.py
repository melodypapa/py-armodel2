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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPSecRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = ARObject._serialize_item(self.direction, "Any")
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
            serialized = ARObject._serialize_item(self.header_type, "IPsecHeaderTypeEnum")
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
            serialized = ARObject._serialize_item(self.ip_protocol, "IPsecIpProtocolEnum")
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
                serialized = ARObject._serialize_item(item, "Any")
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
            serialized = ARObject._serialize_item(self.local_id, "String")
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
            serialized = ARObject._serialize_item(self.local_port_range, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.mode, "IPsecModeEnum")
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
            serialized = ARObject._serialize_item(self.policy, "IPsecPolicyEnum")
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
            serialized = ARObject._serialize_item(self.pre_shared_key_ref, "CryptoServiceKey")
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
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
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
                serialized = ARObject._serialize_item(item, "Any")
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
            serialized = ARObject._serialize_item(self.remote_id, "String")
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
                serialized = ARObject._serialize_item(item, "NetworkEndpoint")
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
            serialized = ARObject._serialize_item(self.remote_port, "PositiveInteger")
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
        child = ARObject._find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = child.text
            obj.direction = direction_value

        # Parse header_type
        child = ARObject._find_child_element(element, "HEADER-TYPE")
        if child is not None:
            header_type_value = IPsecHeaderTypeEnum.deserialize(child)
            obj.header_type = header_type_value

        # Parse ip_protocol
        child = ARObject._find_child_element(element, "IP-PROTOCOL")
        if child is not None:
            ip_protocol_value = IPsecIpProtocolEnum.deserialize(child)
            obj.ip_protocol = ip_protocol_value

        # Parse local_certificate_refs (list from container "LOCAL-CERTIFICATE-REFS")
        obj.local_certificate_refs = []
        container = ARObject._find_child_element(element, "LOCAL-CERTIFICATE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.local_certificate_refs.append(child_value)

        # Parse local_id
        child = ARObject._find_child_element(element, "LOCAL-ID")
        if child is not None:
            local_id_value = child.text
            obj.local_id = local_id_value

        # Parse local_port_range
        child = ARObject._find_child_element(element, "LOCAL-PORT-RANGE")
        if child is not None:
            local_port_range_value = child.text
            obj.local_port_range = local_port_range_value

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = IPsecModeEnum.deserialize(child)
            obj.mode = mode_value

        # Parse policy
        child = ARObject._find_child_element(element, "POLICY")
        if child is not None:
            policy_value = IPsecPolicyEnum.deserialize(child)
            obj.policy = policy_value

        # Parse pre_shared_key_ref
        child = ARObject._find_child_element(element, "PRE-SHARED-KEY-REF")
        if child is not None:
            pre_shared_key_ref_value = ARRef.deserialize(child)
            obj.pre_shared_key_ref = pre_shared_key_ref_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse remote_refs (list from container "REMOTE-REFS")
        obj.remote_refs = []
        container = ARObject._find_child_element(element, "REMOTE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_refs.append(child_value)

        # Parse remote_id
        child = ARObject._find_child_element(element, "REMOTE-ID")
        if child is not None:
            remote_id_value = child.text
            obj.remote_id = remote_id_value

        # Parse remote_ip_refs (list from container "REMOTE-IP-REFS")
        obj.remote_ip_refs = []
        container = ARObject._find_child_element(element, "REMOTE-IP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_ip_refs.append(child_value)

        # Parse remote_port
        child = ARObject._find_child_element(element, "REMOTE-PORT")
        if child is not None:
            remote_port_value = child.text
            obj.remote_port = remote_port_value

        return obj



class IPSecRuleBuilder:
    """Builder for IPSecRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecRule = IPSecRule()

    def build(self) -> IPSecRule:
        """Build and return IPSecRule object.

        Returns:
            IPSecRule instance
        """
        # TODO: Add validation
        return self._obj
