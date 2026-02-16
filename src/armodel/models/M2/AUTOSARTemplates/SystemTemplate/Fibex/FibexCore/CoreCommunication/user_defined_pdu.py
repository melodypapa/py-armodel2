"""UserDefinedPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedPdu(Pdu):
    """AUTOSAR UserDefinedPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cdd_type", None, True, False, None),  # cddType
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedPdu":
        """Create UserDefinedPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedPdu since parent returns ARObject
        return cast("UserDefinedPdu", obj)


class UserDefinedPduBuilder:
    """Builder for UserDefinedPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPdu = UserDefinedPdu()

    def build(self) -> UserDefinedPdu:
        """Build and return UserDefinedPdu object.

        Returns:
            UserDefinedPdu instance
        """
        # TODO: Add validation
        return self._obj
