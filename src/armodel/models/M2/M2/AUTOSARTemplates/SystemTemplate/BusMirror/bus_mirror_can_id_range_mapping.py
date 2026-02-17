"""BusMirrorCanIdRangeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_base": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # destinationBase
        "source_can_id_code": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sourceCanIdCode
        "source_can_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sourceCanId
    }

    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None


class BusMirrorCanIdRangeMappingBuilder:
    """Builder for BusMirrorCanIdRangeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()

    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return BusMirrorCanIdRangeMapping object.

        Returns:
            BusMirrorCanIdRangeMapping instance
        """
        # TODO: Add validation
        return self._obj
