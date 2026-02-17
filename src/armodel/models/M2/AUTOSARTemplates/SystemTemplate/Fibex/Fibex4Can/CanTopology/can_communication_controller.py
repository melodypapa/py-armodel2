"""CanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanCommunicationController(ARObject):
    """AUTOSAR CanCommunicationController."""

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
