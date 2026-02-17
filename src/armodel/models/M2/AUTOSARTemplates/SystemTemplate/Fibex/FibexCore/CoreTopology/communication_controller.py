"""CommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class CommunicationController(ARObject):
    """AUTOSAR CommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "wake_up_by": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeUpBy
    }

    def __init__(self) -> None:
        """Initialize CommunicationController."""
        super().__init__()
        self.wake_up_by: Optional[Boolean] = None


class CommunicationControllerBuilder:
    """Builder for CommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationController = CommunicationController()

    def build(self) -> CommunicationController:
        """Build and return CommunicationController object.

        Returns:
            CommunicationController instance
        """
        # TODO: Add validation
        return self._obj
