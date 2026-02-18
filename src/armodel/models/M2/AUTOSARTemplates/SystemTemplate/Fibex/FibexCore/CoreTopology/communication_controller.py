"""CommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class CommunicationController(ARObject, ABC):
    """AUTOSAR CommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    wake_up_by: Optional[Boolean]
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
