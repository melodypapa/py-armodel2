"""DdsTopicData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 529)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsTopicData(ARObject):
    """AUTOSAR DdsTopicData."""

    topic_data: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsTopicData."""
        super().__init__()
        self.topic_data: Optional[String] = None


class DdsTopicDataBuilder:
    """Builder for DdsTopicData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsTopicData = DdsTopicData()

    def build(self) -> DdsTopicData:
        """Build and return DdsTopicData object.

        Returns:
            DdsTopicData instance
        """
        # TODO: Add validation
        return self._obj
