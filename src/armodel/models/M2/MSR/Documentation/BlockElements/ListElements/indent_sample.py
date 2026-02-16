"""IndentSample AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class IndentSample(ARObject):
    """AUTOSAR IndentSample."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "item_label_pos_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ItemLabelPosEnum,
        ),  # itemLabelPosEnum
        "l2": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LOverviewParagraph,
        ),  # l2
    }

    def __init__(self) -> None:
        """Initialize IndentSample."""
        super().__init__()
        self.item_label_pos_enum: Optional[ItemLabelPosEnum] = None
        self.l2: LOverviewParagraph = None


class IndentSampleBuilder:
    """Builder for IndentSample."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndentSample = IndentSample()

    def build(self) -> IndentSample:
        """Build and return IndentSample object.

        Returns:
            IndentSample instance
        """
        # TODO: Add validation
        return self._obj
