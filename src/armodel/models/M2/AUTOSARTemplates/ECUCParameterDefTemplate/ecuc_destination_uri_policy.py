"""EcucDestinationUriPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucDestinationUriPolicy(ARObject):
    """AUTOSAR EcucDestinationUriPolicy."""

    containers: list[EcucContainerDef]
    destination_uri: Optional[Any]
    parameters: list[EcucParameterDef]
    references: list[Any]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.references: list[Any] = []


class EcucDestinationUriPolicyBuilder:
    """Builder for EcucDestinationUriPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriPolicy = EcucDestinationUriPolicy()

    def build(self) -> EcucDestinationUriPolicy:
        """Build and return EcucDestinationUriPolicy object.

        Returns:
            EcucDestinationUriPolicy instance
        """
        # TODO: Add validation
        return self._obj
