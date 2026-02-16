"""DoIpEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class DoIpEntity(ARObject):
    """AUTOSAR DoIpEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_entity_role_enum", None, False, False, DoIpEntityRoleEnum),  # doIpEntityRoleEnum
    ]

    def __init__(self) -> None:
        """Initialize DoIpEntity."""
        super().__init__()
        self.do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpEntity":
        """Create DoIpEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpEntity since parent returns ARObject
        return cast("DoIpEntity", obj)


class DoIpEntityBuilder:
    """Builder for DoIpEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpEntity = DoIpEntity()

    def build(self) -> DoIpEntity:
        """Build and return DoIpEntity object.

        Returns:
            DoIpEntity instance
        """
        # TODO: Add validation
        return self._obj
