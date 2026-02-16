"""ComponentSeparation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)


class ComponentSeparation(MappingConstraint):
    """AUTOSAR ComponentSeparation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mapping_scope_enum", None, False, False, MappingScopeEnum),  # mappingScopeEnum
    ]

    def __init__(self) -> None:
        """Initialize ComponentSeparation."""
        super().__init__()
        self.mapping_scope_enum: Optional[MappingScopeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ComponentSeparation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentSeparation":
        """Create ComponentSeparation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ComponentSeparation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ComponentSeparation since parent returns ARObject
        return cast("ComponentSeparation", obj)


class ComponentSeparationBuilder:
    """Builder for ComponentSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentSeparation = ComponentSeparation()

    def build(self) -> ComponentSeparation:
        """Build and return ComponentSeparation object.

        Returns:
            ComponentSeparation instance
        """
        # TODO: Add validation
        return self._obj
