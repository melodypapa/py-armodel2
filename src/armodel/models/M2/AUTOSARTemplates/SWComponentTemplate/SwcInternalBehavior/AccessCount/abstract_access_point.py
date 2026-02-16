"""AbstractAccessPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class AbstractAccessPoint(Identifiable):
    """AUTOSAR AbstractAccessPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("return_value", None, False, False, RteApiReturnValueProvisionEnum),  # returnValue
    ]

    def __init__(self) -> None:
        """Initialize AbstractAccessPoint."""
        super().__init__()
        self.return_value: Optional[RteApiReturnValueProvisionEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractAccessPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractAccessPoint":
        """Create AbstractAccessPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractAccessPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractAccessPoint since parent returns ARObject
        return cast("AbstractAccessPoint", obj)


class AbstractAccessPointBuilder:
    """Builder for AbstractAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractAccessPoint = AbstractAccessPoint()

    def build(self) -> AbstractAccessPoint:
        """Build and return AbstractAccessPoint object.

        Returns:
            AbstractAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
