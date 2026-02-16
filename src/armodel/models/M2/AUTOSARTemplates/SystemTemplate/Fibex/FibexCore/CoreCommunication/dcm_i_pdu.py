"""DcmIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)


class DcmIPdu(IPdu):
    """AUTOSAR DcmIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diag_pdu_type", None, False, False, DiagPduType),  # diagPduType
    ]

    def __init__(self) -> None:
        """Initialize DcmIPdu."""
        super().__init__()
        self.diag_pdu_type: Optional[DiagPduType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DcmIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DcmIPdu":
        """Create DcmIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DcmIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DcmIPdu since parent returns ARObject
        return cast("DcmIPdu", obj)


class DcmIPduBuilder:
    """Builder for DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DcmIPdu = DcmIPdu()

    def build(self) -> DcmIPdu:
        """Build and return DcmIPdu object.

        Returns:
            DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
