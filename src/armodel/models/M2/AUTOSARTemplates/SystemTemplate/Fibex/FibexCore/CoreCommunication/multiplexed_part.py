"""MultiplexedPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.segment_position import (
    SegmentPosition,
)


class MultiplexedPart(ARObject):
    """AUTOSAR MultiplexedPart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "segment_positions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SegmentPosition,
        ),  # segmentPositions
    }

    def __init__(self) -> None:
        """Initialize MultiplexedPart."""
        super().__init__()
        self.segment_positions: list[SegmentPosition] = []


class MultiplexedPartBuilder:
    """Builder for MultiplexedPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedPart = MultiplexedPart()

    def build(self) -> MultiplexedPart:
        """Build and return MultiplexedPart object.

        Returns:
            MultiplexedPart instance
        """
        # TODO: Add validation
        return self._obj
