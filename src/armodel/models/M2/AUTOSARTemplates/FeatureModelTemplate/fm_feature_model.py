"""FMFeatureModel AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 21)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureModel(ARElement):
    """AUTOSAR FMFeatureModel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    features: list[FMFeature]
    root: Optional[FMFeature]
    def __init__(self) -> None:
        """Initialize FMFeatureModel."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.root: Optional[FMFeature] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureModel":
        """Deserialize XML element to FMFeatureModel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureModel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse features (list)
        obj.features = []
        for child in ARObject._find_all_child_elements(element, "FEATURES"):
            features_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.features.append(features_value)

        # Parse root
        child = ARObject._find_child_element(element, "ROOT")
        if child is not None:
            root_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.root = root_value

        return obj



class FMFeatureModelBuilder:
    """Builder for FMFeatureModel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureModel = FMFeatureModel()

    def build(self) -> FMFeatureModel:
        """Build and return FMFeatureModel object.

        Returns:
            FMFeatureModel instance
        """
        # TODO: Add validation
        return self._obj
