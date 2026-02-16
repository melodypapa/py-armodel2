"""MultiLanguageOverviewParagraph AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class MultiLanguageOverviewParagraph(ARObject):
    """AUTOSAR MultiLanguageOverviewParagraph."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "l2": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LOverviewParagraph,
        ),  # l2
    }

    def __init__(self) -> None:
        """Initialize MultiLanguageOverviewParagraph."""
        super().__init__()
        self.l2: LOverviewParagraph = None


class MultiLanguageOverviewParagraphBuilder:
    """Builder for MultiLanguageOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageOverviewParagraph = MultiLanguageOverviewParagraph()

    def build(self) -> MultiLanguageOverviewParagraph:
        """Build and return MultiLanguageOverviewParagraph object.

        Returns:
            MultiLanguageOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
