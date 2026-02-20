"""EndToEndDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 205)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 385)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EndToEndDescription(ARObject):
    """AUTOSAR EndToEndDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[NameToken]
    counter_offset: Optional[PositiveInteger]
    crc_offset: Optional[PositiveInteger]
    data_id_mode: Optional[PositiveInteger]
    data_id_nibble: Optional[PositiveInteger]
    data_length: Optional[PositiveInteger]
    max_delta: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndDescription."""
        super().__init__()
        self.category: Optional[NameToken] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[PositiveInteger] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.data_length: Optional[PositiveInteger] = None
        self.max_delta: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_offset
        if self.counter_offset is not None:
            serialized = ARObject._serialize_item(self.counter_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_offset
        if self.crc_offset is not None:
            serialized = ARObject._serialize_item(self.crc_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_mode
        if self.data_id_mode is not None:
            serialized = ARObject._serialize_item(self.data_id_mode, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_nibble
        if self.data_id_nibble is not None:
            serialized = ARObject._serialize_item(self.data_id_nibble, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-NIBBLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_length
        if self.data_length is not None:
            serialized = ARObject._serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = ARObject._serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndDescription":
        """Deserialize XML element to EndToEndDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndDescription object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse counter_offset
        child = ARObject._find_child_element(element, "COUNTER-OFFSET")
        if child is not None:
            counter_offset_value = child.text
            obj.counter_offset = counter_offset_value

        # Parse crc_offset
        child = ARObject._find_child_element(element, "CRC-OFFSET")
        if child is not None:
            crc_offset_value = child.text
            obj.crc_offset = crc_offset_value

        # Parse data_id_mode
        child = ARObject._find_child_element(element, "DATA-ID-MODE")
        if child is not None:
            data_id_mode_value = child.text
            obj.data_id_mode = data_id_mode_value

        # Parse data_id_nibble
        child = ARObject._find_child_element(element, "DATA-ID-NIBBLE")
        if child is not None:
            data_id_nibble_value = child.text
            obj.data_id_nibble = data_id_nibble_value

        # Parse data_length
        child = ARObject._find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse max_delta
        child = ARObject._find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        return obj



class EndToEndDescriptionBuilder:
    """Builder for EndToEndDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndDescription = EndToEndDescription()

    def build(self) -> EndToEndDescription:
        """Build and return EndToEndDescription object.

        Returns:
            EndToEndDescription instance
        """
        # TODO: Add validation
        return self._obj
