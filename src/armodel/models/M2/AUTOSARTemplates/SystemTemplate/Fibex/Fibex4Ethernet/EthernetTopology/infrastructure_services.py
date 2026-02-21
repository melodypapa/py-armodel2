"""InfrastructureServices AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InfrastructureServices, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_entity
        if self.do_ip_entity is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_entity, "DoIpEntity")
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
            serialized = SerializationHelper.serialize_item(self.time, "TimeSynchronization")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InfrastructureServices, cls).deserialize(element)

        # Parse do_ip_entity
        child = SerializationHelper.find_child_element(element, "DO-IP-ENTITY")
        if child is not None:
            do_ip_entity_value = SerializationHelper.deserialize_by_tag(child, "DoIpEntity")
            obj.do_ip_entity = do_ip_entity_value

        # Parse time
        child = SerializationHelper.find_child_element(element, "TIME")
        if child is not None:
            time_value = SerializationHelper.deserialize_by_tag(child, "TimeSynchronization")
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
