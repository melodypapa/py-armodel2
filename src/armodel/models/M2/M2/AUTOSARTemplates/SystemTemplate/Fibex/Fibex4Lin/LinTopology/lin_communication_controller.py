"""LinCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LinCommunicationController(ARObject):
    """AUTOSAR LinCommunicationController."""

    def __init__(self) -> None:
        """Initialize LinCommunicationController."""
        super().__init__()
        self.protocol_version: Optional[String] = None


class LinCommunicationControllerBuilder:
    """Builder for LinCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCommunicationController = LinCommunicationController()

    def build(self) -> LinCommunicationController:
        """Build and return LinCommunicationController object.

        Returns:
            LinCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
