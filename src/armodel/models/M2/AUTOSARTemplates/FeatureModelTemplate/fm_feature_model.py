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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureModel, cls).deserialize(element)

        # Parse features (list from container "FEATURES")
        obj.features = []
        container = ARObject._find_child_element(element, "FEATURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.features.append(child_value)

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
