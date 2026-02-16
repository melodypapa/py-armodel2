"""AbstractVariationRestriction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class AbstractVariationRestriction(ARObject):
    """AUTOSAR AbstractVariationRestriction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("valid_bindings", None, False, True, FullBindingTimeEnum),  # validBindings
        ("variation", None, True, False, None),  # variation
    ]

    def __init__(self) -> None:
        """Initialize AbstractVariationRestriction."""
        super().__init__()
        self.valid_bindings: list[FullBindingTimeEnum] = []
        self.variation: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractVariationRestriction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractVariationRestriction":
        """Create AbstractVariationRestriction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractVariationRestriction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractVariationRestriction since parent returns ARObject
        return cast("AbstractVariationRestriction", obj)


class AbstractVariationRestrictionBuilder:
    """Builder for AbstractVariationRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractVariationRestriction = AbstractVariationRestriction()

    def build(self) -> AbstractVariationRestriction:
        """Build and return AbstractVariationRestriction object.

        Returns:
            AbstractVariationRestriction instance
        """
        # TODO: Add validation
        return self._obj
