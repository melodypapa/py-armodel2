"""CompuConstTextContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class CompuConstTextContent(CompuConstContent):
    """AUTOSAR CompuConstTextContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "vt": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vt
    }

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
