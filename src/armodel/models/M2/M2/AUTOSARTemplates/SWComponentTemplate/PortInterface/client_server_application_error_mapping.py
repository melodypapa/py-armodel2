"""ClientServerApplicationErrorMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)


class ClientServerApplicationErrorMapping(ARObject):
    """AUTOSAR ClientServerApplicationErrorMapping."""

    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application: Optional[ApplicationError] = None
        self.second: Optional[ApplicationError] = None


class ClientServerApplicationErrorMappingBuilder:
    """Builder for ClientServerApplicationErrorMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerApplicationErrorMapping = ClientServerApplicationErrorMapping()

    def build(self) -> ClientServerApplicationErrorMapping:
        """Build and return ClientServerApplicationErrorMapping object.

        Returns:
            ClientServerApplicationErrorMapping instance
        """
        # TODO: Add validation
        return self._obj
