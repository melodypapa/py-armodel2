"""KeywordSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword import (
    Keyword,
)


class KeywordSet(ARElement):
    """AUTOSAR KeywordSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    keywords: list[Keyword]
    def __init__(self) -> None:
        """Initialize KeywordSet."""
        super().__init__()
        self.keywords: list[Keyword] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "KeywordSet":
        """Deserialize XML element to KeywordSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized KeywordSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse keywords (list)
        obj.keywords = []
        for child in ARObject._find_all_child_elements(element, "KEYWORDS"):
            keywords_value = ARObject._deserialize_by_tag(child, "Keyword")
            obj.keywords.append(keywords_value)

        return obj



class KeywordSetBuilder:
    """Builder for KeywordSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: KeywordSet = KeywordSet()

    def build(self) -> KeywordSet:
        """Build and return KeywordSet object.

        Returns:
            KeywordSet instance
        """
        # TODO: Add validation
        return self._obj
