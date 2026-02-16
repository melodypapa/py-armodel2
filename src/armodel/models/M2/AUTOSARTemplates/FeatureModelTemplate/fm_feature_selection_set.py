"""FMFeatureSelectionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection_set import (
    FMFeatureSelectionSet,
)


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("feature_models", None, False, True, FMFeatureModel),  # featureModels
        ("includes", None, False, True, FMFeatureSelectionSet),  # includes
        ("selections", None, False, True, FMFeatureSelection),  # selections
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureSelectionSet."""
        super().__init__()
        self.feature_models: list[FMFeatureModel] = []
        self.includes: list[FMFeatureSelectionSet] = []
        self.selections: list[FMFeatureSelection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureSelectionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelectionSet":
        """Create FMFeatureSelectionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureSelectionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureSelectionSet since parent returns ARObject
        return cast("FMFeatureSelectionSet", obj)


class FMFeatureSelectionSetBuilder:
    """Builder for FMFeatureSelectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelectionSet = FMFeatureSelectionSet()

    def build(self) -> FMFeatureSelectionSet:
        """Build and return FMFeatureSelectionSet object.

        Returns:
            FMFeatureSelectionSet instance
        """
        # TODO: Add validation
        return self._obj
