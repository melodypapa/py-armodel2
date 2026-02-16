"""MultidimensionalTime AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)


class MultidimensionalTime(ARObject):
    """AUTOSAR MultidimensionalTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cse_code", None, True, False, None),  # cseCode
        ("cse_code_factor", None, True, False, None),  # cseCodeFactor
    ]

    def __init__(self) -> None:
        """Initialize MultidimensionalTime."""
        super().__init__()
        self.cse_code: Optional[CseCodeType] = None
        self.cse_code_factor: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultidimensionalTime to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultidimensionalTime":
        """Create MultidimensionalTime from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultidimensionalTime instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultidimensionalTime since parent returns ARObject
        return cast("MultidimensionalTime", obj)


class MultidimensionalTimeBuilder:
    """Builder for MultidimensionalTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultidimensionalTime = MultidimensionalTime()

    def build(self) -> MultidimensionalTime:
        """Build and return MultidimensionalTime object.

        Returns:
            MultidimensionalTime instance
        """
        # TODO: Add validation
        return self._obj
