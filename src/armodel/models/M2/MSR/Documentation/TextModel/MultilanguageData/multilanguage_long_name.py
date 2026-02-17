"""MultilanguageLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 163)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_long_name import (
    LLongName,
)


class MultilanguageLongName(ARObject):
    """AUTOSAR MultilanguageLongName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "l4": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LLongName,
        ),  # l4
    }

    def __init__(self) -> None:
        """Initialize MultilanguageLongName."""
        super().__init__()
        self.l4: LLongName = None


class MultilanguageLongNameBuilder:
    """Builder for MultilanguageLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageLongName = MultilanguageLongName()

    def build(self) -> MultilanguageLongName:
        """Build and return MultilanguageLongName object.

        Returns:
            MultilanguageLongName instance
        """
        # TODO: Add validation
        return self._obj
