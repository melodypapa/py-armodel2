"""BlueprintPolicy AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class BlueprintPolicy(ARObject, ABC):
    """AUTOSAR BlueprintPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute_name: String
    def __init__(self) -> None:
        """Initialize BlueprintPolicy."""
        super().__init__()
        self.attribute_name: String = None


class BlueprintPolicyBuilder:
    """Builder for BlueprintPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintPolicy = BlueprintPolicy()

    def build(self) -> BlueprintPolicy:
        """Build and return BlueprintPolicy object.

        Returns:
            BlueprintPolicy instance
        """
        # TODO: Add validation
        return self._obj
