"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from abc import ABC, abstractmethod


class FMFormulaByFeaturesAndSwSystemconsts(ARObject, ABC):
    """AUTOSAR FMFormulaByFeaturesAndSwSystemconsts."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    feature: Optional[FMFeature]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndSwSystemconsts."""
        super().__init__()
        self.feature: Optional[FMFeature] = None


class FMFormulaByFeaturesAndSwSystemconstsBuilder:
    """Builder for FMFormulaByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndSwSystemconsts = FMFormulaByFeaturesAndSwSystemconsts()

    def build(self) -> FMFormulaByFeaturesAndSwSystemconsts:
        """Build and return FMFormulaByFeaturesAndSwSystemconsts object.

        Returns:
            FMFormulaByFeaturesAndSwSystemconsts instance
        """
        # TODO: Add validation
        return self._obj
