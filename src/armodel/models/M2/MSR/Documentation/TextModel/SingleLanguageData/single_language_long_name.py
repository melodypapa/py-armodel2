"""SingleLanguageLongName AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_SingleLanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SingleLanguageLongName(ARObject):
    """AUTOSAR SingleLanguageLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SingleLanguageLongName."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SingleLanguageLongName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SingleLanguageLongName, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SingleLanguageLongName":
        """Deserialize XML element to SingleLanguageLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SingleLanguageLongName object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SingleLanguageLongName, cls).deserialize(element)



class SingleLanguageLongNameBuilder:
    """Builder for SingleLanguageLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageLongName = SingleLanguageLongName()

    def build(self) -> SingleLanguageLongName:
        """Build and return SingleLanguageLongName object.

        Returns:
            SingleLanguageLongName instance
        """
        # TODO: Add validation
        return self._obj
