"""Compiler AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 133)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 621)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 434)

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


class Compiler(Identifiable):
    """AUTOSAR Compiler."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    name: Optional[String]
    options: Optional[String]
    vendor: Optional[String]
    version: Optional[String]
    def __init__(self) -> None:
        """Initialize Compiler."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None


class CompilerBuilder:
    """Builder for Compiler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compiler = Compiler()

    def build(self) -> Compiler:
        """Build and return Compiler object.

        Returns:
            Compiler instance
        """
        # TODO: Add validation
        return self._obj
