"""TimeSynchronization AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_client_configuration import (
    TimeSyncClientConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class TimeSynchronization(ARObject):
    """AUTOSAR TimeSynchronization."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "time_sync_client_configuration": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeSyncClientConfiguration,
        ),  # timeSyncClientConfiguration
        "time_sync_server_configuration": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeSyncServerConfiguration,
        ),  # timeSyncServerConfiguration
    }

    def __init__(self) -> None:
        """Initialize TimeSynchronization."""
        super().__init__()
        self.time_sync_client_configuration: Optional[TimeSyncClientConfiguration] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None


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
