"""CouplingElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 107)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
    StateDependentFirewall,
)


class CouplingElement(FibexElement):
    """AUTOSAR CouplingElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_ref: Optional[ARRef]
    coupling: Optional[CouplingElement]
    coupling_ports: list[CouplingPort]
    coupling_type: Optional[CouplingElementEnum]
    ecu_instance_ref: Optional[ARRef]
    firewall_rule_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize CouplingElement."""
        super().__init__()
        self.communication_ref: Optional[ARRef] = None
        self.coupling: Optional[CouplingElement] = None
        self.coupling_ports: list[CouplingPort] = []
        self.coupling_type: Optional[CouplingElementEnum] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.firewall_rule_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize CouplingElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_ref
        if self.communication_ref is not None:
            serialized = ARObject._serialize_item(self.communication_ref, "EthernetCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coupling
        if self.coupling is not None:
            serialized = ARObject._serialize_item(self.coupling, "CouplingElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coupling_ports (list to container "COUPLING-PORTS")
        if self.coupling_ports:
            wrapper = ET.Element("COUPLING-PORTS")
            for item in self.coupling_ports:
                serialized = ARObject._serialize_item(item, "CouplingPort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize coupling_type
        if self.coupling_type is not None:
            serialized = ARObject._serialize_item(self.coupling_type, "CouplingElementEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize firewall_rule_refs (list to container "FIREWALL-RULE-REFS")
        if self.firewall_rule_refs:
            wrapper = ET.Element("FIREWALL-RULE-REFS")
            for item in self.firewall_rule_refs:
                serialized = ARObject._serialize_item(item, "StateDependentFirewall")
                if serialized is not None:
                    child_elem = ET.Element("FIREWALL-RULE-REF")
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
    def deserialize(cls, element: ET.Element) -> "CouplingElement":
        """Deserialize XML element to CouplingElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingElement, cls).deserialize(element)

        # Parse communication_ref
        child = ARObject._find_child_element(element, "COMMUNICATION-REF")
        if child is not None:
            communication_ref_value = ARRef.deserialize(child)
            obj.communication_ref = communication_ref_value

        # Parse coupling
        child = ARObject._find_child_element(element, "COUPLING")
        if child is not None:
            coupling_value = ARObject._deserialize_by_tag(child, "CouplingElement")
            obj.coupling = coupling_value

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = ARObject._find_child_element(element, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse coupling_type
        child = ARObject._find_child_element(element, "COUPLING-TYPE")
        if child is not None:
            coupling_type_value = CouplingElementEnum.deserialize(child)
            obj.coupling_type = coupling_type_value

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse firewall_rule_refs (list from container "FIREWALL-RULE-REFS")
        obj.firewall_rule_refs = []
        container = ARObject._find_child_element(element, "FIREWALL-RULE-REFS")
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
                    obj.firewall_rule_refs.append(child_value)

        return obj



class CouplingElementBuilder:
    """Builder for CouplingElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingElement = CouplingElement()

    def build(self) -> CouplingElement:
        """Build and return CouplingElement object.

        Returns:
            CouplingElement instance
        """
        # TODO: Add validation
        return self._obj
