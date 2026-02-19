"""FMFormulaByFeaturesAndAttributes AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from abc import ABC, abstractmethod


class FMFormulaByFeaturesAndAttributes(ARObject, ABC):
    """AUTOSAR FMFormulaByFeaturesAndAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute: Optional[FMAttributeDef]
    feature: Optional[FMFeature]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndAttributes."""
        super().__init__()
        self.attribute: Optional[FMAttributeDef] = None
        self.feature: Optional[FMFeature] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndAttributes":
        """Deserialize XML element to FMFormulaByFeaturesAndAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFormulaByFeaturesAndAttributes object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attribute
        child = ARObject._find_child_element(element, "ATTRIBUTE")
        if child is not None:
            attribute_value = ARObject._deserialize_by_tag(child, "FMAttributeDef")
            obj.attribute = attribute_value

        # Parse feature
        child = ARObject._find_child_element(element, "FEATURE")
        if child is not None:
            feature_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.feature = feature_value

        return obj



class FMFormulaByFeaturesAndAttributesBuilder:
    """Builder for FMFormulaByFeaturesAndAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndAttributes = FMFormulaByFeaturesAndAttributes()

    def build(self) -> FMFormulaByFeaturesAndAttributes:
        """Build and return FMFormulaByFeaturesAndAttributes object.

        Returns:
            FMFormulaByFeaturesAndAttributes instance
        """
        # TODO: Add validation
        return self._obj
