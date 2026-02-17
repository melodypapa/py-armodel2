"""BlueprintPolicyList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BlueprintPolicyList(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # maxNumberOf
        "min_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # minNumberOf
    }

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
