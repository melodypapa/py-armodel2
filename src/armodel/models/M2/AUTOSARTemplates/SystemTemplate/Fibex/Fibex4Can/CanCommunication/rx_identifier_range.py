"""RxIdentifierRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RxIdentifierRange(ARObject):
    """AUTOSAR RxIdentifierRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_can_id: Optional[PositiveInteger]
    upper_can_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize RxIdentifierRange."""
        super().__init__()
        self.lower_can_id: Optional[PositiveInteger] = None
        self.upper_can_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize RxIdentifierRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize lower_can_id
        if self.lower_can_id is not None:
            serialized = ARObject._serialize_item(self.lower_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_can_id
        if self.upper_can_id is not None:
            serialized = ARObject._serialize_item(self.upper_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RxIdentifierRange":
        """Deserialize XML element to RxIdentifierRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RxIdentifierRange object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lower_can_id
        child = ARObject._find_child_element(element, "LOWER-CAN-ID")
        if child is not None:
            lower_can_id_value = child.text
            obj.lower_can_id = lower_can_id_value

        # Parse upper_can_id
        child = ARObject._find_child_element(element, "UPPER-CAN-ID")
        if child is not None:
            upper_can_id_value = child.text
            obj.upper_can_id = upper_can_id_value

        return obj



class RxIdentifierRangeBuilder:
    """Builder for RxIdentifierRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RxIdentifierRange = RxIdentifierRange()

    def build(self) -> RxIdentifierRange:
        """Build and return RxIdentifierRange object.

        Returns:
            RxIdentifierRange instance
        """
        # TODO: Add validation
        return self._obj
