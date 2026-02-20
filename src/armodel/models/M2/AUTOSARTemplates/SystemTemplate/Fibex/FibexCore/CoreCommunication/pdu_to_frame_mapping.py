"""PduToFrameMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)


class PduToFrameMapping(ARObject):
    """AUTOSAR PduToFrameMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    packing_byte: Optional[ByteOrderEnum]
    pdu: Optional[Pdu]
    start_position: Optional[Integer]
    update: Optional[Integer]
    def __init__(self) -> None:
        """Initialize PduToFrameMapping."""
        super().__init__()
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.pdu: Optional[Pdu] = None
        self.start_position: Optional[Integer] = None
        self.update: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize PduToFrameMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize packing_byte
        if self.packing_byte is not None:
            serialized = ARObject._serialize_item(self.packing_byte, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKING-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu
        if self.pdu is not None:
            serialized = ARObject._serialize_item(self.pdu, "Pdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start_position
        if self.start_position is not None:
            serialized = ARObject._serialize_item(self.start_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update
        if self.update is not None:
            serialized = ARObject._serialize_item(self.update, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduToFrameMapping":
        """Deserialize XML element to PduToFrameMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduToFrameMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse packing_byte
        child = ARObject._find_child_element(element, "PACKING-BYTE")
        if child is not None:
            packing_byte_value = ByteOrderEnum.deserialize(child)
            obj.packing_byte = packing_byte_value

        # Parse pdu
        child = ARObject._find_child_element(element, "PDU")
        if child is not None:
            pdu_value = ARObject._deserialize_by_tag(child, "Pdu")
            obj.pdu = pdu_value

        # Parse start_position
        child = ARObject._find_child_element(element, "START-POSITION")
        if child is not None:
            start_position_value = child.text
            obj.start_position = start_position_value

        # Parse update
        child = ARObject._find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



class PduToFrameMappingBuilder:
    """Builder for PduToFrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduToFrameMapping = PduToFrameMapping()

    def build(self) -> PduToFrameMapping:
        """Build and return PduToFrameMapping object.

        Returns:
            PduToFrameMapping instance
        """
        # TODO: Add validation
        return self._obj
