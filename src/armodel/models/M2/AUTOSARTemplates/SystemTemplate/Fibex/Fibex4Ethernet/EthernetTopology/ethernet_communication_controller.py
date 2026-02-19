"""EthernetCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetMacLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    MacAddressString,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class EthernetCommunicationController(ARObject):
    """AUTOSAR EthernetCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_xl_config: Optional[Any]
    coupling_ports: list[CouplingPort]
    mac_layer_type: Optional[EthernetMacLayerTypeEnum]
    mac_unicast: Optional[MacAddressString]
    maximum: Optional[Integer]
    slave_act_as: Optional[Boolean]
    slave_qualified: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationController."""
        super().__init__()
        self.can_xl_config: Optional[Any] = None
        self.coupling_ports: list[CouplingPort] = []
        self.mac_layer_type: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_unicast: Optional[MacAddressString] = None
        self.maximum: Optional[Integer] = None
        self.slave_act_as: Optional[Boolean] = None
        self.slave_qualified: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize EthernetCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize can_xl_config
        if self.can_xl_config is not None:
            serialized = ARObject._serialize_item(self.can_xl_config, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-XL-CONFIG")
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

        # Serialize mac_layer_type
        if self.mac_layer_type is not None:
            serialized = ARObject._serialize_item(self.mac_layer_type, "EthernetMacLayerTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-LAYER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_unicast
        if self.mac_unicast is not None:
            serialized = ARObject._serialize_item(self.mac_unicast, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = ARObject._serialize_item(self.maximum, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave_act_as
        if self.slave_act_as is not None:
            serialized = ARObject._serialize_item(self.slave_act_as, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE-ACT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave_qualified
        if self.slave_qualified is not None:
            serialized = ARObject._serialize_item(self.slave_qualified, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE-QUALIFIED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationController":
        """Deserialize XML element to EthernetCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse can_xl_config
        child = ARObject._find_child_element(element, "CAN-XL-CONFIG")
        if child is not None:
            can_xl_config_value = child.text
            obj.can_xl_config = can_xl_config_value

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = ARObject._find_child_element(element, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse mac_layer_type
        child = ARObject._find_child_element(element, "MAC-LAYER-TYPE")
        if child is not None:
            mac_layer_type_value = EthernetMacLayerTypeEnum.deserialize(child)
            obj.mac_layer_type = mac_layer_type_value

        # Parse mac_unicast
        child = ARObject._find_child_element(element, "MAC-UNICAST")
        if child is not None:
            mac_unicast_value = child.text
            obj.mac_unicast = mac_unicast_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse slave_act_as
        child = ARObject._find_child_element(element, "SLAVE-ACT-AS")
        if child is not None:
            slave_act_as_value = child.text
            obj.slave_act_as = slave_act_as_value

        # Parse slave_qualified
        child = ARObject._find_child_element(element, "SLAVE-QUALIFIED")
        if child is not None:
            slave_qualified_value = child.text
            obj.slave_qualified = slave_qualified_value

        return obj



class EthernetCommunicationControllerBuilder:
    """Builder for EthernetCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCommunicationController = EthernetCommunicationController()

    def build(self) -> EthernetCommunicationController:
        """Build and return EthernetCommunicationController object.

        Returns:
            EthernetCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
