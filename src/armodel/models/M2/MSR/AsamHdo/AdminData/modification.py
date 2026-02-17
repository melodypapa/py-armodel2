"""Modification AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Modification(ARObject):
    """AUTOSAR Modification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "change": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # change
        "reason": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # reason
    }

    def __init__(self) -> None:
        """Initialize Modification."""
        super().__init__()
        self.change: MultiLanguageOverviewParagraph = None
        self.reason: Optional[MultiLanguageOverviewParagraph] = None


class ModificationBuilder:
    """Builder for Modification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Modification = Modification()

    def build(self) -> Modification:
        """Build and return Modification object.

        Returns:
            Modification instance
        """
        # TODO: Add validation
        return self._obj
