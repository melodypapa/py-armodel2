"""EthernetCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class EthernetCluster(ARObject):
    """AUTOSAR EthernetCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupling_port: Optional[TimeValue]
    mac_multicast_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EthernetCluster."""
        super().__init__()
        self.coupling_port: Optional[TimeValue] = None
        self.mac_multicast_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EthernetCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize coupling_port
        if self.coupling_port is not None:
            serialized = ARObject._serialize_item(self.coupling_port, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_multicast_group_refs (list to container "MAC-MULTICAST-GROUPS")
        if self.mac_multicast_group_refs:
            wrapper = ET.Element("MAC-MULTICAST-GROUPS")
            for item in self.mac_multicast_group_refs:
                serialized = ARObject._serialize_item(item, "MacMulticastGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCluster":
        """Deserialize XML element to EthernetCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse coupling_port
        child = ARObject._find_child_element(element, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = child.text
            obj.coupling_port = coupling_port_value

        # Parse mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUPS")
        obj.mac_multicast_group_refs = []
        container = ARObject._find_child_element(element, "MAC-MULTICAST-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mac_multicast_group_refs.append(child_value)

        return obj



class EthernetClusterBuilder:
    """Builder for EthernetCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCluster = EthernetCluster()

    def build(self) -> EthernetCluster:
        """Build and return EthernetCluster object.

        Returns:
            EthernetCluster instance
        """
        # TODO: Add validation
        return self._obj
