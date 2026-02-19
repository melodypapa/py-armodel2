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

        # Parse ordered_masters (list)
        obj.ordered_masters = []
        for child in ARObject._find_all_child_elements(element, "ORDERED-MASTERS"):
            ordered_masters_value = ARObject._deserialize_by_tag(child, "OrderedMaster")
            obj.ordered_masters.append(ordered_masters_value)

        # Parse time_sync
        child = ARObject._find_child_element(element, "TIME-SYNC")
        if child is not None:
            time_sync_value = child.text
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
