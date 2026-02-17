"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFormulaByFeaturesAndSwSystemconsts(ARObject):
    """AUTOSAR FMFormulaByFeaturesAndSwSystemconsts."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "feature": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FMFeature,
        ),  # feature
    }

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
