"""WhitespaceControlled AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class WhitespaceControlled(ARObject, ABC):
    """AUTOSAR WhitespaceControlled."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    xml_space: Any
    def __init__(self) -> None:
        """Initialize WhitespaceControlled."""
        super().__init__()
        self.xml_space: Any = None

    def serialize(self) -> ET.Element:
        """Serialize WhitespaceControlled to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(WhitespaceControlled, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize xml_space
        if self.xml_space is not None:
            serialized = SerializationHelper.serialize_item(self.xml_space, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XML-SPACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "WhitespaceControlled":
        """Deserialize XML element to WhitespaceControlled object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WhitespaceControlled object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WhitespaceControlled, cls).deserialize(element)

        # Parse xml_space
        child = SerializationHelper.find_child_element(element, "XML-SPACE")
        if child is not None:
            xml_space_value = child.text
            obj.xml_space = xml_space_value

        return obj



class WhitespaceControlledBuilder:
    """Builder for WhitespaceControlled."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WhitespaceControlled = WhitespaceControlled()

    def build(self) -> WhitespaceControlled:
        """Build and return WhitespaceControlled object.

        Returns:
            WhitespaceControlled instance
        """
        # TODO: Add validation
        return self._obj
