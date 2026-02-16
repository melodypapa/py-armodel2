"""SwcToImplMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation.swc_implementation import (
    SwcImplementation,
)


class SwcToImplMapping(Identifiable):
    """AUTOSAR SwcToImplMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("component", None, False, False, SwcImplementation),  # component
    ]

    def __init__(self) -> None:
        """Initialize SwcToImplMapping."""
        super().__init__()
        self.component: Optional[SwcImplementation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcToImplMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToImplMapping":
        """Create SwcToImplMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcToImplMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcToImplMapping since parent returns ARObject
        return cast("SwcToImplMapping", obj)


class SwcToImplMappingBuilder:
    """Builder for SwcToImplMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToImplMapping = SwcToImplMapping()

    def build(self) -> SwcToImplMapping:
        """Build and return SwcToImplMapping object.

        Returns:
            SwcToImplMapping instance
        """
        # TODO: Add validation
        return self._obj
