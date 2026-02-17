"""CompuConstTextContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class CompuConstTextContent(CompuConstContent):
    """AUTOSAR CompuConstTextContent."""

    vt: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize CompuConstTextContent."""
        super().__init__()
        self.vt: Optional[VerbatimString] = None


class CompuConstTextContentBuilder:
    """Builder for CompuConstTextContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstTextContent = CompuConstTextContent()

    def build(self) -> CompuConstTextContent:
        """Build and return CompuConstTextContent object.

        Returns:
            CompuConstTextContent instance
        """
        # TODO: Add validation
        return self._obj
