"""HwCategory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwCategory(ARElement):
    """AUTOSAR HwCategory."""

    def __init__(self) -> None:
        """Initialize HwCategory."""
        super().__init__()
        self.hw_attribute_defs: list[HwAttributeDef] = []


class HwCategoryBuilder:
    """Builder for HwCategory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwCategory = HwCategory()

    def build(self) -> HwCategory:
        """Build and return HwCategory object.

        Returns:
            HwCategory instance
        """
        # TODO: Add validation
        return self._obj
