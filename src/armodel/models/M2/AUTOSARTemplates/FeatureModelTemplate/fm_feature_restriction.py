"""FMFeatureRestriction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureRestriction(Identifiable):
    """AUTOSAR FMFeatureRestriction."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("restriction_and_attributes", None, False, False, any (FMConditionByFeatures)),  # restrictionAndAttributes
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureRestriction."""
        super().__init__()
        self.restriction_and_attributes: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureRestriction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRestriction":
        """Create FMFeatureRestriction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureRestriction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureRestriction since parent returns ARObject
        return cast("FMFeatureRestriction", obj)


class FMFeatureRestrictionBuilder:
    """Builder for FMFeatureRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRestriction = FMFeatureRestriction()

    def build(self) -> FMFeatureRestriction:
        """Build and return FMFeatureRestriction object.

        Returns:
            FMFeatureRestriction instance
        """
        # TODO: Add validation
        return self._obj
