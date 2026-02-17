"""LLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LLongName(ARObject):
    """AUTOSAR LLongName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "blueprint_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # blueprintValue
    }

    def __init__(self) -> None:
        """Initialize LLongName."""
        super().__init__()
        self.blueprint_value: Optional[String] = None


class LLongNameBuilder:
    """Builder for LLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LLongName = LLongName()

    def build(self) -> LLongName:
        """Build and return LLongName object.

        Returns:
            LLongName instance
        """
        # TODO: Add validation
        return self._obj
