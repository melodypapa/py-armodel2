"""FMFeatureDecomposition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 27)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureDecomposition(ARObject):
    """AUTOSAR FMFeatureDecomposition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[CategoryString]
    features: list[FMFeature]
    max: Optional[PositiveInteger]
    min: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FMFeatureDecomposition."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.features: list[FMFeature] = []
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureDecomposition":
        """Deserialize XML element to FMFeatureDecomposition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureDecomposition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse features (list)
        obj.features = []
        for child in ARObject._find_all_child_elements(element, "FEATURES"):
            features_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.features.append(features_value)

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class FMFeatureDecompositionBuilder:
    """Builder for FMFeatureDecomposition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureDecomposition = FMFeatureDecomposition()

    def build(self) -> FMFeatureDecomposition:
        """Build and return FMFeatureDecomposition object.

        Returns:
            FMFeatureDecomposition instance
        """
        # TODO: Add validation
        return self._obj
