"""LOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LOverviewParagraph(LanguageSpecific):
    """AUTOSAR LOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LOverviewParagraph."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize LOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes (L attribute and text)
        parent_elem = super(LOverviewParagraph, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Copy text from parent element
        if parent_elem.text is not None:
            elem.text = parent_elem.text

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LOverviewParagraph":
        """Deserialize XML element to LOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LOverviewParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes (L attribute and text)
        return super(LOverviewParagraph, cls).deserialize(element)



class LOverviewParagraphBuilder:
    """Builder for LOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LOverviewParagraph = LOverviewParagraph()

    def build(self) -> LOverviewParagraph:
        """Build and return LOverviewParagraph object.

        Returns:
            LOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
