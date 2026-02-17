"""FormulaExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 223)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 448)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_FormulaLanguage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class FormulaExpression(ARObject):
    """AUTOSAR FormulaExpression."""

    def __init__(self) -> None:
        """Initialize FormulaExpression."""
        super().__init__()
        self.atp_references: list[Referrable] = []
        self.atp_strings: list[Referrable] = []


class FormulaExpressionBuilder:
    """Builder for FormulaExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FormulaExpression = FormulaExpression()

    def build(self) -> FormulaExpression:
        """Build and return FormulaExpression object.

        Returns:
            FormulaExpression instance
        """
        # TODO: Add validation
        return self._obj
