"""BaseType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)


class BaseType(ARElement):
    """AUTOSAR BaseType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_type", None, False, False, BaseTypeDefinition),  # baseType
    ]

    def __init__(self) -> None:
        """Initialize BaseType."""
        super().__init__()
        self.base_type: BaseTypeDefinition = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BaseType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseType":
        """Create BaseType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BaseType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BaseType since parent returns ARObject
        return cast("BaseType", obj)


class BaseTypeBuilder:
    """Builder for BaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseType = BaseType()

    def build(self) -> BaseType:
        """Build and return BaseType object.

        Returns:
            BaseType instance
        """
        # TODO: Add validation
        return self._obj
