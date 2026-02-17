"""AbstractCanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AbstractCanCommunicationController(ARObject):
    """AUTOSAR AbstractCanCommunicationController."""

    can_controller_controller_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationController."""
        super().__init__()
        self.can_controller_controller_attributes: Optional[Any] = None


class AbstractCanCommunicationControllerBuilder:
    """Builder for AbstractCanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationController = AbstractCanCommunicationController()

    def build(self) -> AbstractCanCommunicationController:
        """Build and return AbstractCanCommunicationController object.

        Returns:
            AbstractCanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
