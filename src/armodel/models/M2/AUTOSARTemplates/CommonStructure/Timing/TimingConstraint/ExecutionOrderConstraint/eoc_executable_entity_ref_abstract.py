"""EOCExecutableEntityRefAbstract AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class EOCExecutableEntityRefAbstract(Identifiable):
    """AUTOSAR EOCExecutableEntityRefAbstract."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direct_successors", None, False, True, any (EOCExecutableEntity)),  # directSuccessors
    ]

    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successors: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EOCExecutableEntityRefAbstract to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefAbstract":
        """Create EOCExecutableEntityRefAbstract from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EOCExecutableEntityRefAbstract instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EOCExecutableEntityRefAbstract since parent returns ARObject
        return cast("EOCExecutableEntityRefAbstract", obj)


class EOCExecutableEntityRefAbstractBuilder:
    """Builder for EOCExecutableEntityRefAbstract."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefAbstract = EOCExecutableEntityRefAbstract()

    def build(self) -> EOCExecutableEntityRefAbstract:
        """Build and return EOCExecutableEntityRefAbstract object.

        Returns:
            EOCExecutableEntityRefAbstract instance
        """
        # TODO: Add validation
        return self._obj
