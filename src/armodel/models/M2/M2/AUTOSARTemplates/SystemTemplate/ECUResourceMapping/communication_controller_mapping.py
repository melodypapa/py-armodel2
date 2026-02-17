"""CommunicationControllerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class CommunicationControllerMapping(ARObject):
    """AUTOSAR CommunicationControllerMapping."""

    def __init__(self) -> None:
        """Initialize CommunicationControllerMapping."""
        super().__init__()
        self.communication_controller: Optional[CommunicationController] = None
        self.hw: Optional[HwElement] = None


class CommunicationControllerMappingBuilder:
    """Builder for CommunicationControllerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationControllerMapping = CommunicationControllerMapping()

    def build(self) -> CommunicationControllerMapping:
        """Build and return CommunicationControllerMapping object.

        Returns:
            CommunicationControllerMapping instance
        """
        # TODO: Add validation
        return self._obj
