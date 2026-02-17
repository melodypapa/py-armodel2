"""NumericalRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 467)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR NumericalRuleBasedValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rule_based": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (RuleBasedValue),
        ),  # ruleBased
    }

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
