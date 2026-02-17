"""CanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class CanCommunicationController(ARObject):
    """AUTOSAR CanCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize CanCommunicationController."""
        super().__init__()


class CanCommunicationControllerBuilder:
    """Builder for CanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationController = CanCommunicationController()

    def build(self) -> CanCommunicationController:
        """Build and return CanCommunicationController object.

        Returns:
            CanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
