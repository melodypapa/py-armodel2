"""AbstractValueRestriction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)


class AbstractValueRestriction(ARObject):
    """AUTOSAR AbstractValueRestriction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max", None, True, False, None),  # max
        ("max_length", None, True, False, None),  # maxLength
        ("min", None, True, False, None),  # min
        ("min_length", None, True, False, None),  # minLength
        ("pattern", None, True, False, None),  # pattern
    ]

    def __init__(self) -> None:
        """Initialize AbstractValueRestriction."""
        super().__init__()
        self.max: Optional[Limit] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min: Optional[Limit] = None
        self.min_length: Optional[PositiveInteger] = None
        self.pattern: Optional[RegularExpression] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractValueRestriction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractValueRestriction":
        """Create AbstractValueRestriction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractValueRestriction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractValueRestriction since parent returns ARObject
        return cast("AbstractValueRestriction", obj)


class AbstractValueRestrictionBuilder:
    """Builder for AbstractValueRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractValueRestriction = AbstractValueRestriction()

    def build(self) -> AbstractValueRestriction:
        """Build and return AbstractValueRestriction object.

        Returns:
            AbstractValueRestriction instance
        """
        # TODO: Add validation
        return self._obj
