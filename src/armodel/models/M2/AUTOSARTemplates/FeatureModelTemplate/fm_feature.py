"""FMFeature AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
    FMFeatureRelation,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
    FMFeatureRestriction,
)


class FMFeature(ARElement):
    """AUTOSAR FMFeature."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attribute_defs", None, False, True, FMAttributeDef),  # attributeDefs
        ("decomposition_decompositions", None, False, True, FMFeature),  # decompositionDecompositions
        ("maximum", None, False, False, BindingTimeEnum),  # maximum
        ("minimum", None, False, False, BindingTimeEnum),  # minimum
        ("relations", None, False, True, FMFeatureRelation),  # relations
        ("restrictions", None, False, True, FMFeatureRestriction),  # restrictions
    ]

    def __init__(self) -> None:
        """Initialize FMFeature."""
        super().__init__()
        self.attribute_defs: list[FMAttributeDef] = []
        self.decomposition_decompositions: list[FMFeature] = []
        self.maximum: Optional[BindingTimeEnum] = None
        self.minimum: Optional[BindingTimeEnum] = None
        self.relations: list[FMFeatureRelation] = []
        self.restrictions: list[FMFeatureRestriction] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeature to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeature":
        """Create FMFeature from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeature instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeature since parent returns ARObject
        return cast("FMFeature", obj)


class FMFeatureBuilder:
    """Builder for FMFeature."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeature = FMFeature()

    def build(self) -> FMFeature:
        """Build and return FMFeature object.

        Returns:
            FMFeature instance
        """
        # TODO: Add validation
        return self._obj
