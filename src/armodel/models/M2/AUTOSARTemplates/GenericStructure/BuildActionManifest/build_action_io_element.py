"""BuildActionIoElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionIoElement(ARObject):
    """AUTOSAR BuildActionIoElement."""

    category: NameToken
    ecuc_definition: Optional[EcucDefinitionElement]
    role: Optional[Identifier]
    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize BuildActionIoElement."""
        super().__init__()
        self.category: NameToken = None
        self.ecuc_definition: Optional[EcucDefinitionElement] = None
        self.role: Optional[Identifier] = None
        self.sdgs: list[Sdg] = []


class BuildActionIoElementBuilder:
    """Builder for BuildActionIoElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionIoElement = BuildActionIoElement()

    def build(self) -> BuildActionIoElement:
        """Build and return BuildActionIoElement object.

        Returns:
            BuildActionIoElement instance
        """
        # TODO: Add validation
        return self._obj
