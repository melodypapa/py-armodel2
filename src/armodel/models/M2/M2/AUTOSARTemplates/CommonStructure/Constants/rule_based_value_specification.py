"""RuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_arguments import (
    RuleArguments,
)


class RuleBasedValueSpecification(ARObject):
    """AUTOSAR RuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize RuleBasedValueSpecification."""
        super().__init__()
        self.arguments: Optional[RuleArguments] = None
        self.max_size_to_fill: Optional[Integer] = None
        self.rule: Optional[Identifier] = None


class RuleBasedValueSpecificationBuilder:
    """Builder for RuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueSpecification = RuleBasedValueSpecification()

    def build(self) -> RuleBasedValueSpecification:
        """Build and return RuleBasedValueSpecification object.

        Returns:
            RuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
