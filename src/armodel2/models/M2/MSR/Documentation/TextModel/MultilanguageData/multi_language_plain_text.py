"""MultiLanguagePlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import lang_prefix

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_plain_text import (
    LPlainText,
)


class MultiLanguagePlainText(ARObject):
    """AUTOSAR MultiLanguagePlainText."""

    _XML_TAG = "MULTI-LANGUAGE-PLAIN-TEXT"

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _l10: list[LPlainText]
    def __init__(self) -> None:
        """Initialize MultiLanguagePlainText."""
        super().__init__()
        self._l10: list[LPlainText] = []
    @property
    @lang_prefix("L-10")
    def l10(self) -> list[LPlainText]:
        """Get l10 with language-specific wrapper."""
        return self._l10

    @l10.setter
    def l10(self, value: list[LPlainText]) -> None:
        """Set l10 with language-specific wrapper."""
        self._l10 = value

    def serialize(self) -> ET.Element:
        """Serialize MultiLanguagePlainText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # First, call parent's serialize to handle inherited attributes (timestamp and checksum)
        parent_elem = super(MultiLanguagePlainText, self).serialize()

        elem = ET.Element(self._XML_TAG)

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize l10 (list to container "L-10")
        if self._l10:
            for item in self._l10:
                # Create L-10 element with L attribute from LPlainText
                wrapper = ET.Element("L-10")
                if item.l is not None:
                    wrapper.set("L", str(item.l))
                # Copy text content from LPlainText
                if item._text is not None:
                    wrapper.text = item._text
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguagePlainText":
        """Deserialize XML element to MultiLanguagePlainText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguagePlainText object
        """
        # First, call parent's deserialize to handle inherited attributes (timestamp and checksum)
        obj = super(MultiLanguagePlainText, cls).deserialize(element)

        # Deserialize l10 list from L-10 elements
        obj._l10 = []
        for child in element:
            if SerializationHelper.strip_namespace(child.tag) == "L-10":
                # Create LPlainText item from L-10 element
                l10_item = LPlainText()
                # Extract L attribute
                l_value = child.get("L")
                if l_value is not None:
                    l10_item.l = l_value
                # Extract text content
                if child.text is not None and child.text.strip():
                    l10_item._text = child.text
                obj._l10.append(l10_item)

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
