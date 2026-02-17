"""ClientServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 155)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerAnnotation(GeneralAnnotation):
    """AUTOSAR ClientServerAnnotation."""

    operation: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientServerAnnotation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None


class ClientServerAnnotationBuilder:
    """Builder for ClientServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerAnnotation = ClientServerAnnotation()

    def build(self) -> ClientServerAnnotation:
        """Build and return ClientServerAnnotation object.

        Returns:
            ClientServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
