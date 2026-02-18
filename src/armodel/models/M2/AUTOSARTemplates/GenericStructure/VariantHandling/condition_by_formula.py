"""ConditionByFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 231)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)


class ConditionByFormula(ARObject):
    """AUTOSAR ConditionByFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    binding_time_enum: BindingTimeEnum
    def __init__(self) -> None:
        """Initialize ConditionByFormula."""
        super().__init__()
        self.binding_time_enum: BindingTimeEnum = None


class ConditionByFormulaBuilder:
    """Builder for ConditionByFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionByFormula = ConditionByFormula()

    def build(self) -> ConditionByFormula:
        """Build and return ConditionByFormula object.

        Returns:
            ConditionByFormula instance
        """
        # TODO: Add validation
        return self._obj
