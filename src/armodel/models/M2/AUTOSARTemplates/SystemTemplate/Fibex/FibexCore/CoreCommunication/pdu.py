"""Pdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)


class Pdu(FibexElement):
    """AUTOSAR Pdu."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("has_dynamic", None, True, False, None),  # hasDynamic
        ("length", None, True, False, None),  # length
    ]

    def __init__(self) -> None:
        """Initialize Pdu."""
        super().__init__()
        self.has_dynamic: Optional[Boolean] = None
        self.length: Optional[UnlimitedInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Pdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Pdu":
        """Create Pdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Pdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Pdu since parent returns ARObject
        return cast("Pdu", obj)


class PduBuilder:
    """Builder for Pdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Pdu = Pdu()

    def build(self) -> Pdu:
        """Build and return Pdu object.

        Returns:
            Pdu instance
        """
        # TODO: Add validation
        return self._obj
