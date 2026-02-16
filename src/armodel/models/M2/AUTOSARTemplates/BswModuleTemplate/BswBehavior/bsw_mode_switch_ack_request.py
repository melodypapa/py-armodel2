"""BswModeSwitchAckRequest AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswModeSwitchAckRequest(ARObject):
    """AUTOSAR BswModeSwitchAckRequest."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize BswModeSwitchAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModeSwitchAckRequest to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchAckRequest":
        """Create BswModeSwitchAckRequest from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModeSwitchAckRequest instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModeSwitchAckRequest since parent returns ARObject
        return cast("BswModeSwitchAckRequest", obj)


class BswModeSwitchAckRequestBuilder:
    """Builder for BswModeSwitchAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchAckRequest = BswModeSwitchAckRequest()

    def build(self) -> BswModeSwitchAckRequest:
        """Build and return BswModeSwitchAckRequest object.

        Returns:
            BswModeSwitchAckRequest instance
        """
        # TODO: Add validation
        return self._obj
