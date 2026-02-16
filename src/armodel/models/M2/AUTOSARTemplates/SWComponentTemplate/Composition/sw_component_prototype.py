"""SwComponentPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type", None, False, False, SwComponentType),  # type
    ]

    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type: Optional[SwComponentType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwComponentPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototype":
        """Create SwComponentPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwComponentPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwComponentPrototype since parent returns ARObject
        return cast("SwComponentPrototype", obj)


class SwComponentPrototypeBuilder:
    """Builder for SwComponentPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototype = SwComponentPrototype()

    def build(self) -> SwComponentPrototype:
        """Build and return SwComponentPrototype object.

        Returns:
            SwComponentPrototype instance
        """
        # TODO: Add validation
        return self._obj
