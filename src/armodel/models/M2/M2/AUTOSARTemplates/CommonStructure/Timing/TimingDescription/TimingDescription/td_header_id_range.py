"""TDHeaderIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDHeaderIdRange(ARObject):
    """AUTOSAR TDHeaderIdRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_header_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxHeaderId
        "min_header_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minHeaderId
    }

    def __init__(self) -> None:
        """Initialize TDHeaderIdRange."""
        super().__init__()
        self.max_header_id: Optional[Integer] = None
        self.min_header_id: Optional[Integer] = None


class TDHeaderIdRangeBuilder:
    """Builder for TDHeaderIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDHeaderIdRange = TDHeaderIdRange()

    def build(self) -> TDHeaderIdRange:
        """Build and return TDHeaderIdRange object.

        Returns:
            TDHeaderIdRange instance
        """
        # TODO: Add validation
        return self._obj
