"""CouplingPortConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class CouplingPortConnection(ARObject):
    """AUTOSAR CouplingPortConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_port: Optional[CouplingPort]
    node_ports: list[CouplingPort]
    plca_local_node: Optional[PositiveInteger]
    plca_transmit: Optional[PositiveInteger]
    second_port: Optional[CouplingPort]
    def __init__(self) -> None:
        """Initialize CouplingPortConnection."""
        super().__init__()
        self.first_port: Optional[CouplingPort] = None
        self.node_ports: list[CouplingPort] = []
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_transmit: Optional[PositiveInteger] = None
        self.second_port: Optional[CouplingPort] = None
    def serialize(self) -> ET.Element:
        """Serialize CouplingPortConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize first_port
        if self.first_port is not None:
            serialized = ARObject._serialize_item(self.first_port, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_ports (list to container "NODE-PORTS")
        if self.node_ports:
            wrapper = ET.Element("NODE-PORTS")
            for item in self.node_ports:
                serialized = ARObject._serialize_item(item, "CouplingPort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize plca_local_node
        if self.plca_local_node is not None:
            serialized = ARObject._serialize_item(self.plca_local_node, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLCA-LOCAL-NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize plca_transmit
        if self.plca_transmit is not None:
            serialized = ARObject._serialize_item(self.plca_transmit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLCA-TRANSMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_port
        if self.second_port is not None:
            serialized = ARObject._serialize_item(self.second_port, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortConnection":
        """Deserialize XML element to CouplingPortConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_port
        child = ARObject._find_child_element(element, "FIRST-PORT")
        if child is not None:
            first_port_value = ARObject._deserialize_by_tag(child, "CouplingPort")
            obj.first_port = first_port_value

        # Parse node_ports (list from container "NODE-PORTS")
        obj.node_ports = []
        container = ARObject._find_child_element(element, "NODE-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.node_ports.append(child_value)

        # Parse plca_local_node
        child = ARObject._find_child_element(element, "PLCA-LOCAL-NODE")
        if child is not None:
            plca_local_node_value = child.text
            obj.plca_local_node = plca_local_node_value

        # Parse plca_transmit
        child = ARObject._find_child_element(element, "PLCA-TRANSMIT")
        if child is not None:
            plca_transmit_value = child.text
            obj.plca_transmit = plca_transmit_value

        # Parse second_port
        child = ARObject._find_child_element(element, "SECOND-PORT")
        if child is not None:
            second_port_value = ARObject._deserialize_by_tag(child, "CouplingPort")
            obj.second_port = second_port_value

        return obj



class CouplingPortConnectionBuilder:
    """Builder for CouplingPortConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortConnection = CouplingPortConnection()

    def build(self) -> CouplingPortConnection:
        """Build and return CouplingPortConnection object.

        Returns:
            CouplingPortConnection instance
        """
        # TODO: Add validation
        return self._obj
