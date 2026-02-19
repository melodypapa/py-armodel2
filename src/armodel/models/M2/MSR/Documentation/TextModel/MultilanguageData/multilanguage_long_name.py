"""MultilanguageLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 163)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_long_name import (
    LLongName,
)


class MultilanguageLongName(ARObject):
    """AUTOSAR MultilanguageLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    l4: LLongName
    def __init__(self) -> None:
        """Initialize MultilanguageLongName."""
        super().__init__()
        self.l4: LLongName = None
    def serialize(self) -> ET.Element:
        """Serialize MultilanguageLongName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize l4
        if self.l4 is not None:
            serialized = ARObject._serialize_item(self.l4, "LLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("L4")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageLongName":
        """Deserialize XML element to MultilanguageLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultilanguageLongName object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse l4
        child = ARObject._find_child_element(element, "L4")
        if child is not None:
            l4_value = ARObject._deserialize_by_tag(child, "LLongName")
            obj.l4 = l4_value

        return obj



class MultilanguageLongNameBuilder:
    """Builder for MultilanguageLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageLongName = MultilanguageLongName()

    def build(self) -> MultilanguageLongName:
        """Build and return MultilanguageLongName object.

        Returns:
            MultilanguageLongName instance
        """
        # TODO: Add validation
        return self._obj
