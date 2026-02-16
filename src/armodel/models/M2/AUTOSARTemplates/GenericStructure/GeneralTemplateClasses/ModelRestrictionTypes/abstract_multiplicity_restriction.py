"""AbstractMultiplicityRestriction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class AbstractMultiplicityRestriction(ARObject):
    """AUTOSAR AbstractMultiplicityRestriction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_multiplicity", None, True, False, None),  # lowerMultiplicity
        ("upper_multiplicity", None, True, False, None),  # upperMultiplicity
    ]

    def __init__(self) -> None:
        """Initialize AbstractMultiplicityRestriction."""
        super().__init__()
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractMultiplicityRestriction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractMultiplicityRestriction":
        """Create AbstractMultiplicityRestriction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractMultiplicityRestriction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractMultiplicityRestriction since parent returns ARObject
        return cast("AbstractMultiplicityRestriction", obj)


class AbstractMultiplicityRestrictionBuilder:
    """Builder for AbstractMultiplicityRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractMultiplicityRestriction = AbstractMultiplicityRestriction()

    def build(self) -> AbstractMultiplicityRestriction:
        """Build and return AbstractMultiplicityRestriction object.

        Returns:
            AbstractMultiplicityRestriction instance
        """
        # TODO: Add validation
        return self._obj
