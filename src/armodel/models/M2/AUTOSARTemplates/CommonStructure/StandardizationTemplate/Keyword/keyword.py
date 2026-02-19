"""Keyword AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 454)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class Keyword(Identifiable):
    """AUTOSAR Keyword."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    abbr_name: NameToken
    classifications: list[NameToken]
    def __init__(self) -> None:
        """Initialize Keyword."""
        super().__init__()
        self.abbr_name: NameToken = None
        self.classifications: list[NameToken] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Keyword":
        """Deserialize XML element to Keyword object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Keyword object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Keyword, cls).deserialize(element)

        # Parse abbr_name
        child = ARObject._find_child_element(element, "ABBR-NAME")
        if child is not None:
            abbr_name_value = child.text
            obj.abbr_name = abbr_name_value

        # Parse classifications (list from container "CLASSIFICATIONS")
        obj.classifications = []
        container = ARObject._find_child_element(element, "CLASSIFICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.classifications.append(child_value)

        return obj



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
