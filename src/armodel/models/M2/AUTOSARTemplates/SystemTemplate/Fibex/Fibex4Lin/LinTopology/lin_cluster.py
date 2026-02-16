"""LinCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class LinCluster(ARObject):
    """AUTOSAR LinCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize LinCluster."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCluster":
        """Create LinCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinCluster since parent returns ARObject
        return cast("LinCluster", obj)


class LinClusterBuilder:
    """Builder for LinCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCluster = LinCluster()

    def build(self) -> LinCluster:
        """Build and return LinCluster object.

        Returns:
            LinCluster instance
        """
        # TODO: Add validation
        return self._obj
