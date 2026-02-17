"""Linker AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Linker(Identifiable):
    """AUTOSAR Linker."""

    name: Optional[String]
    options: Optional[String]
    vendor: Optional[String]
    version: Optional[String]
    def __init__(self) -> None:
        """Initialize Linker."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None


class LinkerBuilder:
    """Builder for Linker."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Linker = Linker()

    def build(self) -> Linker:
        """Build and return Linker object.

        Returns:
            Linker instance
        """
        # TODO: Add validation
        return self._obj
