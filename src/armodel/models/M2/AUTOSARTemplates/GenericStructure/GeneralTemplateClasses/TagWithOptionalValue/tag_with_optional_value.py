"""TagWithOptionalValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 477)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_TagWithOptionalValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class TagWithOptionalValue(ARObject):
    """AUTOSAR TagWithOptionalValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    key: Optional[String]
    sequence_offset: Optional[Integer]
    value: Optional[String]
    def __init__(self) -> None:
        """Initialize TagWithOptionalValue."""
        super().__init__()
        self.key: Optional[String] = None
        self.sequence_offset: Optional[Integer] = None
        self.value: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize TagWithOptionalValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize key
        if self.key is not None:
            serialized = SerializationHelper.serialize_item(self.key, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sequence_offset
        if self.sequence_offset is not None:
            serialized = SerializationHelper.serialize_item(self.sequence_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEQUENCE-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TagWithOptionalValue":
        """Deserialize XML element to TagWithOptionalValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TagWithOptionalValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse key
        child = SerializationHelper.find_child_element(element, "KEY")
        if child is not None:
            key_value = child.text
            obj.key = key_value

        # Parse sequence_offset
        child = SerializationHelper.find_child_element(element, "SEQUENCE-OFFSET")
        if child is not None:
            sequence_offset_value = child.text
            obj.sequence_offset = sequence_offset_value

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class TagWithOptionalValueBuilder:
    """Builder for TagWithOptionalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TagWithOptionalValue = TagWithOptionalValue()

    def build(self) -> TagWithOptionalValue:
        """Build and return TagWithOptionalValue object.

        Returns:
            TagWithOptionalValue instance
        """
        # TODO: Add validation
        return self._obj
