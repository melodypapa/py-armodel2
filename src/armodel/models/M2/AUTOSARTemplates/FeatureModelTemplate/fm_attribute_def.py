"""FMAttributeDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)


class FMAttributeDef(Identifiable):
    """AUTOSAR FMAttributeDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, True, False, None),  # defaultValue
        ("max", None, True, False, None),  # max
        ("min", None, True, False, None),  # min
    ]

    def __init__(self) -> None:
        """Initialize FMAttributeDef."""
        super().__init__()
        self.default_value: Optional[Numerical] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMAttributeDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMAttributeDef":
        """Create FMAttributeDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMAttributeDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMAttributeDef since parent returns ARObject
        return cast("FMAttributeDef", obj)


class FMAttributeDefBuilder:
    """Builder for FMAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeDef = FMAttributeDef()

    def build(self) -> FMAttributeDef:
        """Build and return FMAttributeDef object.

        Returns:
            FMAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
