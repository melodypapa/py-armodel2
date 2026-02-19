"""FMFeatureSelectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature_models: list[FMFeatureModel]
    include_refs: list[ARRef]
    selections: list[FMFeatureSelection]
    def __init__(self) -> None:
        """Initialize FMFeatureSelectionSet."""
        super().__init__()
        self.feature_models: list[FMFeatureModel] = []
        self.include_refs: list[ARRef] = []
        self.selections: list[FMFeatureSelection] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelectionSet":
        """Deserialize XML element to FMFeatureSelectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureSelectionSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse feature_models (list)
        obj.feature_models = []
        for child in ARObject._find_all_child_elements(element, "FEATURE-MODELS"):
            feature_models_value = ARObject._deserialize_by_tag(child, "FMFeatureModel")
            obj.feature_models.append(feature_models_value)

        # Parse include_refs (list)
        obj.include_refs = []
        for child in ARObject._find_all_child_elements(element, "INCLUDES"):
            include_refs_value = ARObject._deserialize_by_tag(child, "FMFeatureSelectionSet")
            obj.include_refs.append(include_refs_value)

        # Parse selections (list)
        obj.selections = []
        for child in ARObject._find_all_child_elements(element, "SELECTIONS"):
            selections_value = ARObject._deserialize_by_tag(child, "FMFeatureSelection")
            obj.selections.append(selections_value)

        return obj



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
