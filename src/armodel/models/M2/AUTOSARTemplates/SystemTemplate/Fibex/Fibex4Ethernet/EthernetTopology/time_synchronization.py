"""TimeSynchronization AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_client_configuration import (
    TimeSyncClientConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class TimeSynchronization(ARObject):
    """AUTOSAR TimeSynchronization."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    time_sync_client_configuration: Optional[TimeSyncClientConfiguration]
    time_sync_server_configuration: Optional[TimeSyncServerConfiguration]
    def __init__(self) -> None:
        """Initialize TimeSynchronization."""
        super().__init__()
        self.time_sync_client_configuration: Optional[TimeSyncClientConfiguration] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSynchronization":
        """Deserialize XML element to TimeSynchronization object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSynchronization object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse time_sync_client_configuration
        child = ARObject._find_child_element(element, "TIME-SYNC-CLIENT-CONFIGURATION")
        if child is not None:
            time_sync_client_configuration_value = ARObject._deserialize_by_tag(child, "TimeSyncClientConfiguration")
            obj.time_sync_client_configuration = time_sync_client_configuration_value

        # Parse time_sync_server_configuration
        child = ARObject._find_child_element(element, "TIME-SYNC-SERVER-CONFIGURATION")
        if child is not None:
            time_sync_server_configuration_value = ARObject._deserialize_by_tag(child, "TimeSyncServerConfiguration")
            obj.time_sync_server_configuration = time_sync_server_configuration_value

        return obj



class TimeSynchronizationBuilder:
    """Builder for TimeSynchronization."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSynchronization = TimeSynchronization()

    def build(self) -> TimeSynchronization:
        """Build and return TimeSynchronization object.

        Returns:
            TimeSynchronization instance
        """
        # TODO: Add validation
        return self._obj
