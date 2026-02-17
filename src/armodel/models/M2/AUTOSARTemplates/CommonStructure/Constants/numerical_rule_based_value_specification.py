"""NumericalRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 467)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR NumericalRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize NumericalRuleBasedValueSpecification."""
        super().__init__()
        self.rule_based: Optional[Any] = None


class NumericalRuleBasedValueSpecificationBuilder:
    """Builder for NumericalRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalRuleBasedValueSpecification = NumericalRuleBasedValueSpecification()

    def build(self) -> NumericalRuleBasedValueSpecification:
        """Build and return NumericalRuleBasedValueSpecification object.

        Returns:
            NumericalRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
