"""MultiLanguageOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 53)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 347)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class MultiLanguageOverviewParagraph(ARObject):
    """AUTOSAR MultiLanguageOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    l2: LOverviewParagraph
    def __init__(self) -> None:
        """Initialize MultiLanguageOverviewParagraph."""
        super().__init__()
        self.l2: LOverviewParagraph = None
    def serialize(self) -> ET.Element:
        """Serialize MultiLanguageOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize l2
        if self.l2 is not None:
            serialized = ARObject._serialize_item(self.l2, "LOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("L2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageOverviewParagraph":
        """Deserialize XML element to MultiLanguageOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageOverviewParagraph object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse l2
        child = ARObject._find_child_element(element, "L2")
        if child is not None:
            l2_value = ARObject._deserialize_by_tag(child, "LOverviewParagraph")
            obj.l2 = l2_value

        return obj



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
