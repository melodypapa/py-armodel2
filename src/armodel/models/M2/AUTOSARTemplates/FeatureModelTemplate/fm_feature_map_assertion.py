"""FMFeatureMapAssertion AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureMapAssertion(Identifiable):
    """AUTOSAR FMFeatureMapAssertion."""

    fm_syscond_and_sw_systemconsts: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureMapAssertion."""
        super().__init__()
        self.fm_syscond_and_sw_systemconsts: Optional[Any] = None


class FMFeatureMapAssertionBuilder:
    """Builder for FMFeatureMapAssertion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapAssertion = FMFeatureMapAssertion()

    def build(self) -> FMFeatureMapAssertion:
        """Build and return FMFeatureMapAssertion object.

        Returns:
            FMFeatureMapAssertion instance
        """
        # TODO: Add validation
        return self._obj
