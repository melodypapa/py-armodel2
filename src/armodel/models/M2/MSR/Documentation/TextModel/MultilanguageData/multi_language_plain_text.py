"""MultiLanguagePlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_plain_text import (
    LPlainText,
)


class MultiLanguagePlainText(ARObject):
    """AUTOSAR MultiLanguagePlainText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    l10: LPlainText
    def __init__(self) -> None:
        """Initialize MultiLanguagePlainText."""
        super().__init__()
        self.l10: LPlainText = None
    def serialize(self) -> ET.Element:
        """Serialize MultiLanguagePlainText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize l10 - use L-10 (language-specific element with hyphen)
        if self.l10 is not None:
            serialized = ARObject._serialize_item(self.l10, "LPlainText")
            if serialized is not None:
                # Wrap with correct tag L-10 (language-specific)
                wrapped = ET.Element("L-10")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguagePlainText":
        """Deserialize XML element to MultiLanguagePlainText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguagePlainText object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse l10 - look for L-10 (language-specific element with hyphen)
        child = ARObject._find_child_element(element, "L-10")
        if child is not None:
            l10_value = ARObject._deserialize_by_tag(child, "LPlainText")
            obj.l10 = l10_value

        return obj



class MultiLanguagePlainTextBuilder:
    """Builder for MultiLanguagePlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguagePlainText = MultiLanguagePlainText()

    def build(self) -> MultiLanguagePlainText:
        """Build and return MultiLanguagePlainText object.

        Returns:
            MultiLanguagePlainText instance
        """
        # TODO: Add validation
        return self._obj
