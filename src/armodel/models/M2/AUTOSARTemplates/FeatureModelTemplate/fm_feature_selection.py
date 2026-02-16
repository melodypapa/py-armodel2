"""FMFeatureSelection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
    FMAttributeValue,
)


class FMFeatureSelection(Identifiable):
    """AUTOSAR FMFeatureSelection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attribute_values", None, False, True, FMAttributeValue),  # attributeValues
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureSelection."""
        super().__init__()
        self.attribute_values: list[FMAttributeValue] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureSelection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelection":
        """Create FMFeatureSelection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureSelection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureSelection since parent returns ARObject
        return cast("FMFeatureSelection", obj)


class FMFeatureSelectionBuilder:
    """Builder for FMFeatureSelection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelection = FMFeatureSelection()

    def build(self) -> FMFeatureSelection:
        """Build and return FMFeatureSelection object.

        Returns:
            FMFeatureSelection instance
        """
        # TODO: Add validation
        return self._obj
