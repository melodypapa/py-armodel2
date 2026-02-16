"""AclOperation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.acl_operation import (
    AclOperation,
)


class AclOperation(ARElement):
    """AUTOSAR AclOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implieds", None, False, True, AclOperation),  # implieds
    ]

    def __init__(self) -> None:
        """Initialize AclOperation."""
        super().__init__()
        self.implieds: list[AclOperation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AclOperation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclOperation":
        """Create AclOperation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AclOperation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AclOperation since parent returns ARObject
        return cast("AclOperation", obj)


class AclOperationBuilder:
    """Builder for AclOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclOperation = AclOperation()

    def build(self) -> AclOperation:
        """Build and return AclOperation object.

        Returns:
            AclOperation instance
        """
        # TODO: Add validation
        return self._obj
