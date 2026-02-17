"""RxIdentifierRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RxIdentifierRange(ARObject):
    """AUTOSAR RxIdentifierRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lower_can_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # lowerCanId
        "upper_can_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperCanId
    }

    def __init__(self) -> None:
        """Initialize RxIdentifierRange."""
        super().__init__()
        self.lower_can_id: Optional[PositiveInteger] = None
        self.upper_can_id: Optional[PositiveInteger] = None


class RxIdentifierRangeBuilder:
    """Builder for RxIdentifierRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RxIdentifierRange = RxIdentifierRange()

    def build(self) -> RxIdentifierRange:
        """Build and return RxIdentifierRange object.

        Returns:
            RxIdentifierRange instance
        """
        # TODO: Add validation
        return self._obj
