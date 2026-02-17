"""TimeSyncServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class TimeSyncServerConfiguration(Referrable):
    """AUTOSAR TimeSyncServerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "sync_interval": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncInterval
        "time_sync_server_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeSyncServerIdentifier
        "time_sync": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeSyncTechnologyEnum,
        ),  # timeSync
    }

    def __init__(self) -> None:
        """Initialize TimeSyncServerConfiguration."""
        super().__init__()
        self.priority: Optional[PositiveInteger] = None
        self.sync_interval: Optional[TimeValue] = None
        self.time_sync_server_identifier: Optional[String] = None
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None


class TimeSyncServerConfigurationBuilder:
    """Builder for TimeSyncServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSyncServerConfiguration = TimeSyncServerConfiguration()

    def build(self) -> TimeSyncServerConfiguration:
        """Build and return TimeSyncServerConfiguration object.

        Returns:
            TimeSyncServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
