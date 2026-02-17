"""DdsCpISignalToDdsTopicMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 293)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)


class DdsCpISignalToDdsTopicMapping(ARObject):
    """AUTOSAR DdsCpISignalToDdsTopicMapping."""

    dds_topic: Optional[DdsCpTopic]
    i_signal: Optional[ISignal]
    def __init__(self) -> None:
        """Initialize DdsCpISignalToDdsTopicMapping."""
        super().__init__()
        self.dds_topic: Optional[DdsCpTopic] = None
        self.i_signal: Optional[ISignal] = None


class DdsCpISignalToDdsTopicMappingBuilder:
    """Builder for DdsCpISignalToDdsTopicMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpISignalToDdsTopicMapping = DdsCpISignalToDdsTopicMapping()

    def build(self) -> DdsCpISignalToDdsTopicMapping:
        """Build and return DdsCpISignalToDdsTopicMapping object.

        Returns:
            DdsCpISignalToDdsTopicMapping instance
        """
        # TODO: Add validation
        return self._obj
