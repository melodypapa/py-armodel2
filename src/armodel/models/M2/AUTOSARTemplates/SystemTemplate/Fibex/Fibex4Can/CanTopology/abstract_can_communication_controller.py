"""AbstractCanCommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class AbstractCanCommunicationController(ARObject):
    """AUTOSAR AbstractCanCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("can_controller_controller_attributes", None, False, False, any (AbstractCan)),  # canControllerControllerAttributes
    ]

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationController."""
        super().__init__()
        self.can_controller_controller_attributes: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractCanCommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationController":
        """Create AbstractCanCommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractCanCommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractCanCommunicationController since parent returns ARObject
        return cast("AbstractCanCommunicationController", obj)


class AbstractCanCommunicationControllerBuilder:
    """Builder for AbstractCanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationController = AbstractCanCommunicationController()

    def build(self) -> AbstractCanCommunicationController:
        """Build and return AbstractCanCommunicationController object.

        Returns:
            AbstractCanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
