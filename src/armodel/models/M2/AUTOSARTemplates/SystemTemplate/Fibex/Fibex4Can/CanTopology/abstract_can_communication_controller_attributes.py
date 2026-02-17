"""AbstractCanCommunicationControllerAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AbstractCanCommunicationControllerAttributes(ARObject):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None


class AbstractCanCommunicationControllerAttributesBuilder:
    """Builder for AbstractCanCommunicationControllerAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()

    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return AbstractCanCommunicationControllerAttributes object.

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # TODO: Add validation
        return self._obj
