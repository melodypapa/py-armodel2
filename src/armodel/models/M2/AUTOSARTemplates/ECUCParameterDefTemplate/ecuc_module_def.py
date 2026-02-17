"""EcucModuleDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 32)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucModuleDef(EcucDefinitionElement):
    """AUTOSAR EcucModuleDef."""

    api_service_prefix: Optional[CIdentifier]
    containers: list[EcucContainerDef]
    post_build_variant: Optional[Boolean]
    refined_module: Optional[EcucModuleDef]
    supporteds: list[Any]
    def __init__(self) -> None:
        """Initialize EcucModuleDef."""
        super().__init__()
        self.api_service_prefix: Optional[CIdentifier] = None
        self.containers: list[EcucContainerDef] = []
        self.post_build_variant: Optional[Boolean] = None
        self.refined_module: Optional[EcucModuleDef] = None
        self.supporteds: list[Any] = []


class EcucModuleDefBuilder:
    """Builder for EcucModuleDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleDef = EcucModuleDef()

    def build(self) -> EcucModuleDef:
        """Build and return EcucModuleDef object.

        Returns:
            EcucModuleDef instance
        """
        # TODO: Add validation
        return self._obj
