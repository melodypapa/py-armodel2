"""FMFeatureMapCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureMapCondition(Identifiable):
    """AUTOSAR FMFeatureMapCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fm_cond_and_attributes", None, False, False, any (FMConditionByFeatures)),  # fmCondAndAttributes
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureMapCondition."""
        super().__init__()
        self.fm_cond_and_attributes: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureMapCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapCondition":
        """Create FMFeatureMapCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureMapCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureMapCondition since parent returns ARObject
        return cast("FMFeatureMapCondition", obj)


class FMFeatureMapConditionBuilder:
    """Builder for FMFeatureMapCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapCondition = FMFeatureMapCondition()

    def build(self) -> FMFeatureMapCondition:
        """Build and return FMFeatureMapCondition object.

        Returns:
            FMFeatureMapCondition instance
        """
        # TODO: Add validation
        return self._obj
