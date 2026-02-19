"""OrderedMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class OrderedMaster(ARObject):
    """AUTOSAR OrderedMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    index: Optional[PositiveInteger]
    time_sync_server_configuration: Optional[TimeSyncServerConfiguration]
    def __init__(self) -> None:
        """Initialize OrderedMaster."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "OrderedMaster":
        """Deserialize XML element to OrderedMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OrderedMaster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        # Parse time_sync_server_configuration
        child = ARObject._find_child_element(element, "TIME-SYNC-SERVER-CONFIGURATION")
        if child is not None:
            time_sync_server_configuration_value = ARObject._deserialize_by_tag(child, "TimeSyncServerConfiguration")
            obj.time_sync_server_configuration = time_sync_server_configuration_value

        return obj



class OrderedMasterBuilder:
    """Builder for OrderedMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OrderedMaster = OrderedMaster()

    def build(self) -> OrderedMaster:
        """Build and return OrderedMaster object.

        Returns:
            OrderedMaster instance
        """
        # TODO: Add validation
        return self._obj
