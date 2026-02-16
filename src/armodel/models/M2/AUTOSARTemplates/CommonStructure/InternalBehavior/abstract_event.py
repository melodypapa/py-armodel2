"""AbstractEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class AbstractEvent(Identifiable):
    """AUTOSAR AbstractEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("activation", None, False, False, ExecutableEntity),  # activation
    ]

    def __init__(self) -> None:
        """Initialize AbstractEvent."""
        super().__init__()
        self.activation: Optional[ExecutableEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEvent":
        """Create AbstractEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractEvent since parent returns ARObject
        return cast("AbstractEvent", obj)


class AbstractEventBuilder:
    """Builder for AbstractEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEvent = AbstractEvent()

    def build(self) -> AbstractEvent:
        """Build and return AbstractEvent object.

        Returns:
            AbstractEvent instance
        """
        # TODO: Add validation
        return self._obj
