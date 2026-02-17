"""UserDefinedCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedCommunicationController(ARObject):
    """AUTOSAR UserDefinedCommunicationController."""

    def __init__(self) -> None:
        """Initialize UserDefinedCommunicationController."""
        super().__init__()


class UserDefinedCommunicationControllerBuilder:
    """Builder for UserDefinedCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCommunicationController = UserDefinedCommunicationController()

    def build(self) -> UserDefinedCommunicationController:
        """Build and return UserDefinedCommunicationController object.

        Returns:
            UserDefinedCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
