"""HwAttributeDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_literal_def import (
    HwAttributeLiteralDef,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class HwAttributeDef(Identifiable):
    """AUTOSAR HwAttributeDef."""

    hw_attributes: list[HwAttributeLiteralDef]
    is_required: Optional[Boolean]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize HwAttributeDef."""
        super().__init__()
        self.hw_attributes: list[HwAttributeLiteralDef] = []
        self.is_required: Optional[Boolean] = None
        self.unit: Optional[Unit] = None


class HwAttributeDefBuilder:
    """Builder for HwAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeDef = HwAttributeDef()

    def build(self) -> HwAttributeDef:
        """Build and return HwAttributeDef object.

        Returns:
            HwAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
