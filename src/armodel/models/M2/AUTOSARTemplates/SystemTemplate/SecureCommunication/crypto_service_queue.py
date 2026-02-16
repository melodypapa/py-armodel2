"""CryptoServiceQueue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceQueue(ARElement):
    """AUTOSAR CryptoServiceQueue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("queue_size", None, True, False, None),  # queueSize
    ]

    def __init__(self) -> None:
        """Initialize CryptoServiceQueue."""
        super().__init__()
        self.queue_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoServiceQueue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceQueue":
        """Create CryptoServiceQueue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoServiceQueue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoServiceQueue since parent returns ARObject
        return cast("CryptoServiceQueue", obj)


class CryptoServiceQueueBuilder:
    """Builder for CryptoServiceQueue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceQueue = CryptoServiceQueue()

    def build(self) -> CryptoServiceQueue:
        """Build and return CryptoServiceQueue object.

        Returns:
            CryptoServiceQueue instance
        """
        # TODO: Add validation
        return self._obj
