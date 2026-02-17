"""DdsTopicData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 529)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsTopicData(ARObject):
    """AUTOSAR DdsTopicData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "topic_data": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # topicData
    }

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
