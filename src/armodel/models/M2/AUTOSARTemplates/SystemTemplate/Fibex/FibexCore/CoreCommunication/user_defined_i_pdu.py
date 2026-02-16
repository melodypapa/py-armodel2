"""UserDefinedIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedIPdu(IPdu):
    """AUTOSAR UserDefinedIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cdd_type", None, True, False, None),  # cddType
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedIPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedIPdu":
        """Create UserDefinedIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedIPdu since parent returns ARObject
        return cast("UserDefinedIPdu", obj)


class UserDefinedIPduBuilder:
    """Builder for UserDefinedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedIPdu = UserDefinedIPdu()

    def build(self) -> UserDefinedIPdu:
        """Build and return UserDefinedIPdu object.

        Returns:
            UserDefinedIPdu instance
        """
        # TODO: Add validation
        return self._obj
