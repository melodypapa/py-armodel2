"""FMConditionByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FMConditionByFeaturesAndSwSystemconsts(ARObject):
    """AUTOSAR FMConditionByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize FMConditionByFeaturesAndSwSystemconsts."""
        super().__init__()


class FMConditionByFeaturesAndSwSystemconstsBuilder:
    """Builder for FMConditionByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMConditionByFeaturesAndSwSystemconsts = FMConditionByFeaturesAndSwSystemconsts()

    def build(self) -> FMConditionByFeaturesAndSwSystemconsts:
        """Build and return FMConditionByFeaturesAndSwSystemconsts object.

        Returns:
            FMConditionByFeaturesAndSwSystemconsts instance
        """
        # TODO: Add validation
        return self._obj
