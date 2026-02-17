"""BlueprintPolicyNotModifiable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)


class BlueprintPolicyNotModifiable(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyNotModifiable."""

    def __init__(self) -> None:
        """Initialize BlueprintPolicyNotModifiable."""
        super().__init__()


class BlueprintPolicyNotModifiableBuilder:
    """Builder for BlueprintPolicyNotModifiable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicyNotModifiable = BlueprintPolicyNotModifiable()

    def build(self) -> BlueprintPolicyNotModifiable:
        """Build and return BlueprintPolicyNotModifiable object.

        Returns:
            BlueprintPolicyNotModifiable instance
        """
        # TODO: Add validation
        return self._obj
