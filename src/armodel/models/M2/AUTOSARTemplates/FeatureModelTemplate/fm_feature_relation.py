"""FMFeatureRelation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureRelation(Identifiable):
    """AUTOSAR FMFeatureRelation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("features", None, False, True, FMFeature),  # features
        ("restriction", None, False, False, any (FMConditionByFeatures)),  # restriction
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.restriction: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureRelation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRelation":
        """Create FMFeatureRelation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureRelation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureRelation since parent returns ARObject
        return cast("FMFeatureRelation", obj)


class FMFeatureRelationBuilder:
    """Builder for FMFeatureRelation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRelation = FMFeatureRelation()

    def build(self) -> FMFeatureRelation:
        """Build and return FMFeatureRelation object.

        Returns:
            FMFeatureRelation instance
        """
        # TODO: Add validation
        return self._obj
