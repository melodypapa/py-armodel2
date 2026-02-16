"""ModeSwitchedAckRequest AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ModeSwitchedAckRequest(ARObject):
    """AUTOSAR ModeSwitchedAckRequest."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchedAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchedAckRequest to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchedAckRequest":
        """Create ModeSwitchedAckRequest from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchedAckRequest instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchedAckRequest since parent returns ARObject
        return cast("ModeSwitchedAckRequest", obj)


class ModeSwitchedAckRequestBuilder:
    """Builder for ModeSwitchedAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchedAckRequest = ModeSwitchedAckRequest()

    def build(self) -> ModeSwitchedAckRequest:
        """Build and return ModeSwitchedAckRequest object.

        Returns:
            ModeSwitchedAckRequest instance
        """
        # TODO: Add validation
        return self._obj
