"""TimeSyncClientConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ordered_master import (
    OrderedMaster,
)


class TimeSyncClientConfiguration(ARObject):
    """AUTOSAR TimeSyncClientConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ordered_masters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=OrderedMaster,
        ),  # orderedMasters
        "time_sync": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeSyncTechnologyEnum,
        ),  # timeSync
    }

    def __init__(self) -> None:
        """Initialize TimeSyncClientConfiguration."""
        super().__init__()
        self.ordered_masters: list[OrderedMaster] = []
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None


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
