"""ComponentClustering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)


class ComponentClustering(MappingConstraint):
    """AUTOSAR ComponentClustering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("clustereds", None, False, True, any (SwComponent)),  # clustereds
        ("mapping_scope_enum", None, False, False, MappingScopeEnum),  # mappingScopeEnum
    ]

    def __init__(self) -> None:
        """Initialize ComponentClustering."""
        super().__init__()
        self.clustereds: list[Any] = []
        self.mapping_scope_enum: Optional[MappingScopeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ComponentClustering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentClustering":
        """Create ComponentClustering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ComponentClustering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ComponentClustering since parent returns ARObject
        return cast("ComponentClustering", obj)


class ComponentClusteringBuilder:
    """Builder for ComponentClustering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentClustering = ComponentClustering()

    def build(self) -> ComponentClustering:
        """Build and return ComponentClustering object.

        Returns:
            ComponentClustering instance
        """
        # TODO: Add validation
        return self._obj
