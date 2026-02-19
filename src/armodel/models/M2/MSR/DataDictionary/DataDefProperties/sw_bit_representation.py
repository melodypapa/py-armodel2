"""SwBitRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 333)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SwBitRepresentation(ARObject):
    """AUTOSAR SwBitRepresentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_position: Optional[Integer]
    number_of_bits: Optional[Integer]
    def __init__(self) -> None:
        """Initialize SwBitRepresentation."""
        super().__init__()
        self.bit_position: Optional[Integer] = None
        self.number_of_bits: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize SwBitRepresentation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize bit_position
        if self.bit_position is not None:
            serialized = ARObject._serialize_item(self.bit_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize number_of_bits
        if self.number_of_bits is not None:
            serialized = ARObject._serialize_item(self.number_of_bits, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER-OF-BITS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwBitRepresentation":
        """Deserialize XML element to SwBitRepresentation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwBitRepresentation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bit_position
        child = ARObject._find_child_element(element, "BIT-POSITION")
        if child is not None:
            bit_position_value = child.text
            obj.bit_position = bit_position_value

        # Parse number_of_bits
        child = ARObject._find_child_element(element, "NUMBER-OF-BITS")
        if child is not None:
            number_of_bits_value = child.text
            obj.number_of_bits = number_of_bits_value

        return obj



class SwBitRepresentationBuilder:
    """Builder for SwBitRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBitRepresentation = SwBitRepresentation()

    def build(self) -> SwBitRepresentation:
        """Build and return SwBitRepresentation object.

        Returns:
            SwBitRepresentation instance
        """
        # TODO: Add validation
        return self._obj
