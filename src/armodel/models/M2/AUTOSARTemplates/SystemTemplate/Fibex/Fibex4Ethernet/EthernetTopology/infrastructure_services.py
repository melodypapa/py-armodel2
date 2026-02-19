"""InfrastructureServices AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
    DoIpEntity,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
    TimeSynchronization,
)


class InfrastructureServices(ARObject):
    """AUTOSAR InfrastructureServices."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_entity: Optional[DoIpEntity]
    time: Optional[TimeSynchronization]
    def __init__(self) -> None:
        """Initialize InfrastructureServices."""
        super().__init__()
        self.do_ip_entity: Optional[DoIpEntity] = None
        self.time: Optional[TimeSynchronization] = None
    def serialize(self) -> ET.Element:
        """Serialize InfrastructureServices to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize do_ip_entity
        if self.do_ip_entity is not None:
            serialized = ARObject._serialize_item(self.do_ip_entity, "DoIpEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time
        if self.time is not None:
            serialized = ARObject._serialize_item(self.time, "TimeSynchronization")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InfrastructureServices":
        """Deserialize XML element to InfrastructureServices object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InfrastructureServices object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse do_ip_entity
        child = ARObject._find_child_element(element, "DO-IP-ENTITY")
        if child is not None:
            do_ip_entity_value = ARObject._deserialize_by_tag(child, "DoIpEntity")
            obj.do_ip_entity = do_ip_entity_value

        # Parse time
        child = ARObject._find_child_element(element, "TIME")
        if child is not None:
            time_value = ARObject._deserialize_by_tag(child, "TimeSynchronization")
            obj.time = time_value

        return obj



class InfrastructureServicesBuilder:
    """Builder for InfrastructureServices."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InfrastructureServices = InfrastructureServices()

    def build(self) -> InfrastructureServices:
        """Build and return InfrastructureServices object.

        Returns:
            InfrastructureServices instance
        """
        # TODO: Add validation
        return self._obj
