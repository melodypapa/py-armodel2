"""AbstractCanCommunicationControllerAttributes AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class AbstractCanCommunicationControllerAttributes(ARObject):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("can_controller_fd", None, False, False, any (CanControllerFd)),  # canControllerFd
        ("can_controller_xl", None, False, False, any (CanControllerXl)),  # canControllerXl
    ]

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractCanCommunicationControllerAttributes to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationControllerAttributes":
        """Create AbstractCanCommunicationControllerAttributes from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractCanCommunicationControllerAttributes since parent returns ARObject
        return cast("AbstractCanCommunicationControllerAttributes", obj)


class AbstractCanCommunicationControllerAttributesBuilder:
    """Builder for AbstractCanCommunicationControllerAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()

    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return AbstractCanCommunicationControllerAttributes object.

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # TODO: Add validation
        return self._obj
