"""Keyword AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 454)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class Keyword(Identifiable):
    """AUTOSAR Keyword."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "abbr_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # abbrName
        "classifications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # classifications
    }

    def __init__(self) -> None:
        """Initialize Keyword."""
        super().__init__()
        self.abbr_name: NameToken = None
        self.classifications: list[NameToken] = []


class KeywordBuilder:
    """Builder for Keyword."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Keyword = Keyword()

    def build(self) -> Keyword:
        """Build and return Keyword object.

        Returns:
            Keyword instance
        """
        # TODO: Add validation
        return self._obj
