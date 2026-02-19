"""DoIpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    doip_interfaces: list[DoIpInterface]
    logic_address: Optional[DoIpLogicAddress]
    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None
    def serialize(self) -> ET.Element:
        """Serialize DoIpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize doip_interfaces (list to container "DOIP-INTERFACES")
        if self.doip_interfaces:
            wrapper = ET.Element("DOIP-INTERFACES")
            for item in self.doip_interfaces:
                serialized = ARObject._serialize_item(item, "DoIpInterface")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize logic_address
        if self.logic_address is not None:
            serialized = ARObject._serialize_item(self.logic_address, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOGIC-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpConfig":
        """Deserialize XML element to DoIpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse doip_interfaces (list from container "DOIP-INTERFACES")
        obj.doip_interfaces = []
        container = ARObject._find_child_element(element, "DOIP-INTERFACES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.doip_interfaces.append(child_value)

        # Parse logic_address
        child = ARObject._find_child_element(element, "LOGIC-ADDRESS")
        if child is not None:
            logic_address_value = ARObject._deserialize_by_tag(child, "DoIpLogicAddress")
            obj.logic_address = logic_address_value

        return obj



class DoIpConfigBuilder:
    """Builder for DoIpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpConfig = DoIpConfig()

    def build(self) -> DoIpConfig:
        """Build and return DoIpConfig object.

        Returns:
            DoIpConfig instance
        """
        # TODO: Add validation
        return self._obj
