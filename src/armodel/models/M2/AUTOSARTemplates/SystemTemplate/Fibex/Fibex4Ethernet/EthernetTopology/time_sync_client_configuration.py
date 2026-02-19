"""TimeSyncClientConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ordered_master import (
    OrderedMaster,
)


class TimeSyncClientConfiguration(ARObject):
    """AUTOSAR TimeSyncClientConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ordered_masters: list[OrderedMaster]
    time_sync: Optional[TimeSyncTechnologyEnum]
    def __init__(self) -> None:
        """Initialize TimeSyncClientConfiguration."""
        super().__init__()
        self.ordered_masters: list[OrderedMaster] = []
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize TimeSyncClientConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize ordered_masters (list to container "ORDERED-MASTERS")
        if self.ordered_masters:
            wrapper = ET.Element("ORDERED-MASTERS")
            for item in self.ordered_masters:
                serialized = ARObject._serialize_item(item, "OrderedMaster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize time_sync
        if self.time_sync is not None:
            serialized = ARObject._serialize_item(self.time_sync, "TimeSyncTechnologyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncClientConfiguration":
        """Deserialize XML element to TimeSyncClientConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSyncClientConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ordered_masters (list from container "ORDERED-MASTERS")
        obj.ordered_masters = []
        container = ARObject._find_child_element(element, "ORDERED-MASTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ordered_masters.append(child_value)

        # Parse time_sync
        child = ARObject._find_child_element(element, "TIME-SYNC")
        if child is not None:
            time_sync_value = TimeSyncTechnologyEnum.deserialize(child)
            obj.time_sync = time_sync_value

        return obj



class TimeSyncClientConfigurationBuilder:
    """Builder for TimeSyncClientConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSyncClientConfiguration = TimeSyncClientConfiguration()

    def build(self) -> TimeSyncClientConfiguration:
        """Build and return TimeSyncClientConfiguration object.

        Returns:
            TimeSyncClientConfiguration instance
        """
        # TODO: Add validation
        return self._obj
