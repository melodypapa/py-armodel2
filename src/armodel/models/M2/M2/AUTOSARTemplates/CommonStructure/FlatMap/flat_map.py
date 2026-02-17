"""FlatMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 965)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 445)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)


class FlatMap(ARElement):
    """AUTOSAR FlatMap."""

    def __init__(self) -> None:
        """Initialize FlatMap."""
        super().__init__()
        self.instances: list[FlatInstanceDescriptor] = []


class FlatMapBuilder:
    """Builder for FlatMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlatMap = FlatMap()

    def build(self) -> FlatMap:
        """Build and return FlatMap object.

        Returns:
            FlatMap instance
        """
        # TODO: Add validation
        return self._obj
