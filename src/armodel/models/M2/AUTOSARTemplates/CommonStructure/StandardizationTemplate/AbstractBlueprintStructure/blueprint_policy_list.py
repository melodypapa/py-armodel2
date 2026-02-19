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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BlueprintPolicyList(BlueprintPolicy):
    """AUTOSAR BlueprintPolicyList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: PositiveInteger
    min_number_of: PositiveInteger
    def __init__(self) -> None:
        """Initialize BlueprintPolicyList."""
        super().__init__()
        self.max_number_of: PositiveInteger = None
        self.min_number_of: PositiveInteger = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicyList":
        """Deserialize XML element to BlueprintPolicyList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintPolicyList object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse min_number_of
        child = ARObject._find_child_element(element, "MIN-NUMBER-OF")
        if child is not None:
            min_number_of_value = child.text
            obj.min_number_of = min_number_of_value

        return obj



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
