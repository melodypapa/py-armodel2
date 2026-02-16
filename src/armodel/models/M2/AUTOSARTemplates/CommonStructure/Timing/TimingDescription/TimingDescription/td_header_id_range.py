"""TDHeaderIdRange AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDHeaderIdRange(ARObject):
    """AUTOSAR TDHeaderIdRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_header_id", None, True, False, None),  # maxHeaderId
        ("min_header_id", None, True, False, None),  # minHeaderId
    ]

    def __init__(self) -> None:
        """Initialize TDHeaderIdRange."""
        super().__init__()
        self.max_header_id: Optional[Integer] = None
        self.min_header_id: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDHeaderIdRange to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDHeaderIdRange":
        """Create TDHeaderIdRange from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDHeaderIdRange instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDHeaderIdRange since parent returns ARObject
        return cast("TDHeaderIdRange", obj)


class TDHeaderIdRangeBuilder:
    """Builder for TDHeaderIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDHeaderIdRange = TDHeaderIdRange()

    def build(self) -> TDHeaderIdRange:
        """Build and return TDHeaderIdRange object.

        Returns:
            TDHeaderIdRange instance
        """
        # TODO: Add validation
        return self._obj
