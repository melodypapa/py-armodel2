"""FMFeatureMapElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
    FMFeatureMap,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assertions", None, False, True, FMFeatureMap),  # assertions
        ("conditions", None, False, True, FMFeatureMap),  # conditions
        ("post_build_variants", None, False, True, any (PostBuildVariant)),  # postBuildVariants
        ("sw_value_sets", None, False, True, SwSystemconstantValueSet),  # swValueSets
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variants: list[Any] = []
        self.sw_value_sets: list[SwSystemconstantValueSet] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureMapElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapElement":
        """Create FMFeatureMapElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureMapElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureMapElement since parent returns ARObject
        return cast("FMFeatureMapElement", obj)


class FMFeatureMapElementBuilder:
    """Builder for FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapElement = FMFeatureMapElement()

    def build(self) -> FMFeatureMapElement:
        """Build and return FMFeatureMapElement object.

        Returns:
            FMFeatureMapElement instance
        """
        # TODO: Add validation
        return self._obj
