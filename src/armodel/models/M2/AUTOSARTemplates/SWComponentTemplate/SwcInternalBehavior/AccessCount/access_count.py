"""AccessCount AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AccessCount(ARObject):
    """AUTOSAR AccessCount."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access_point", None, False, False, AbstractAccessPoint),  # accessPoint
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize AccessCount."""
        super().__init__()
        self.access_point: Optional[AbstractAccessPoint] = None
        self.value: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AccessCount to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCount":
        """Create AccessCount from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AccessCount instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AccessCount since parent returns ARObject
        return cast("AccessCount", obj)


class AccessCountBuilder:
    """Builder for AccessCount."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCount = AccessCount()

    def build(self) -> AccessCount:
        """Build and return AccessCount object.

        Returns:
            AccessCount instance
        """
        # TODO: Add validation
        return self._obj
