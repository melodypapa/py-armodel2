"""Caption AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Caption(MultilanguageReferrable):
    """AUTOSAR Caption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    desc: Optional[MultiLanguageOverviewParagraph]
    def __init__(self) -> None:
        """Initialize Caption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Caption":
        """Deserialize XML element to Caption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Caption object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Caption, cls).deserialize(element)

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        return obj



class CaptionBuilder:
    """Builder for Caption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Caption = Caption()

    def build(self) -> Caption:
        """Build and return Caption object.

        Returns:
            Caption instance
        """
        # TODO: Add validation
        return self._obj
