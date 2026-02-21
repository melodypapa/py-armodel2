"""LPlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class LPlainText(LanguageSpecific):
    """AUTOSAR LPlainText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LPlainText."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize LPlainText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes (L attribute and text)
        parent_elem = super(LPlainText, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "LPlainText":
        """Deserialize XML element to LPlainText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LPlainText object
        """
        # First, call parent's deserialize to handle inherited attributes (L attribute and text)
        return super(LPlainText, cls).deserialize(element)



class LPlainTextBuilder:
    """Builder for LPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LPlainText = LPlainText()

    def build(self) -> LPlainText:
        """Build and return LPlainText object.

        Returns:
            LPlainText instance
        """
        # TODO: Add validation
        return self._obj