"""CompositeRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR CompositeRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueSpecification."""
        super().__init__()
        self.arguments: list[CompositeValueSpecification] = []
        self.compounds: list[Any] = []
        self.max_size_to_fill: Optional[PositiveInteger] = None
        self.rule: Optional[Identifier] = None


class CompositeRuleBasedValueSpecificationBuilder:
    """Builder for CompositeRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeRuleBasedValueSpecification = CompositeRuleBasedValueSpecification()

    def build(self) -> CompositeRuleBasedValueSpecification:
        """Build and return CompositeRuleBasedValueSpecification object.

        Returns:
            CompositeRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
