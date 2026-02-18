"""ApplicationRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 462)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_rule_based_value_argument import (
    CompositeRuleBasedValueArgument,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_based_axis_cont import (
    RuleBasedAxisCont,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_based_value_cont import (
    RuleBasedValueCont,
)


class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """AUTOSAR ApplicationRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category_specification: Optional[Identifier]
    sw_axis_conts: list[RuleBasedAxisCont]
    sw_value_cont: Optional[RuleBasedValueCont]
    def __init__(self) -> None:
        """Initialize ApplicationRuleBasedValueSpecification."""
        super().__init__()
        self.category_specification: Optional[Identifier] = None
        self.sw_axis_conts: list[RuleBasedAxisCont] = []
        self.sw_value_cont: Optional[RuleBasedValueCont] = None


class ApplicationRuleBasedValueSpecificationBuilder:
    """Builder for ApplicationRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRuleBasedValueSpecification = ApplicationRuleBasedValueSpecification()

    def build(self) -> ApplicationRuleBasedValueSpecification:
        """Build and return ApplicationRuleBasedValueSpecification object.

        Returns:
            ApplicationRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
