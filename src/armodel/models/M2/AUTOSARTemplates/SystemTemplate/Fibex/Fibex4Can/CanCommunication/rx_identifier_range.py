"""RxIdentifierRange AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RxIdentifierRange(ARObject):
    """AUTOSAR RxIdentifierRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_can_id", None, True, False, None),  # lowerCanId
        ("upper_can_id", None, True, False, None),  # upperCanId
    ]

    def __init__(self) -> None:
        """Initialize RxIdentifierRange."""
        super().__init__()
        self.lower_can_id: Optional[PositiveInteger] = None
        self.upper_can_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RxIdentifierRange to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RxIdentifierRange":
        """Create RxIdentifierRange from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RxIdentifierRange instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RxIdentifierRange since parent returns ARObject
        return cast("RxIdentifierRange", obj)


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
