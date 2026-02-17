"""BlueprintPolicyList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BlueprintPolicyList(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyList."""

    def __init__(self) -> None:
        """Initialize BlueprintPolicyList."""
        super().__init__()
        self.max_number_of: PositiveInteger = None
        self.min_number_of: PositiveInteger = None


class BlueprintPolicyListBuilder:
    """Builder for BlueprintPolicyList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicyList = BlueprintPolicyList()

    def build(self) -> BlueprintPolicyList:
        """Build and return BlueprintPolicyList object.

        Returns:
            BlueprintPolicyList instance
        """
        # TODO: Add validation
        return self._obj
