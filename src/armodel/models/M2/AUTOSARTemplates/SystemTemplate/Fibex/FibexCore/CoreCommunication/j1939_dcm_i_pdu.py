"""J1939DcmIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class J1939DcmIPdu(IPdu):
    """AUTOSAR J1939DcmIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic", None, True, False, None),  # diagnostic
        ("message_type", None, False, False, any (e.g)),  # MessageType
    ]

    def __init__(self) -> None:
        """Initialize J1939DcmIPdu."""
        super().__init__()
        self.diagnostic: Optional[PositiveInteger] = None
        self.message_type: Any = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939DcmIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939DcmIPdu":
        """Create J1939DcmIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939DcmIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939DcmIPdu since parent returns ARObject
        return cast("J1939DcmIPdu", obj)


class J1939DcmIPduBuilder:
    """Builder for J1939DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939DcmIPdu = J1939DcmIPdu()

    def build(self) -> J1939DcmIPdu:
        """Build and return J1939DcmIPdu object.

        Returns:
            J1939DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
