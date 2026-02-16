"""UserDefinedCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class UserDefinedCluster(ARObject):
    """AUTOSAR UserDefinedCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedCluster."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedCluster":
        """Create UserDefinedCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedCluster since parent returns ARObject
        return cast("UserDefinedCluster", obj)


class UserDefinedClusterBuilder:
    """Builder for UserDefinedCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCluster = UserDefinedCluster()

    def build(self) -> UserDefinedCluster:
        """Build and return UserDefinedCluster object.

        Returns:
            UserDefinedCluster instance
        """
        # TODO: Add validation
        return self._obj
