"""AtpBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from abc import ABC, abstractmethod


class AtpBlueprint(Identifiable, ABC):
    """AUTOSAR AtpBlueprint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    blueprint_policies: list[BlueprintPolicy]
    def __init__(self) -> None:
        """Initialize AtpBlueprint."""
        super().__init__()
        self.blueprint_policies: list[BlueprintPolicy] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprint":
        """Deserialize XML element to AtpBlueprint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpBlueprint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint_policies (list)
        obj.blueprint_policies = []
        for child in ARObject._find_all_child_elements(element, "BLUEPRINT-POLICIES"):
            blueprint_policies_value = ARObject._deserialize_by_tag(child, "BlueprintPolicy")
            obj.blueprint_policies.append(blueprint_policies_value)

        return obj



class AtpBlueprintBuilder:
    """Builder for AtpBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprint = AtpBlueprint()

    def build(self) -> AtpBlueprint:
        """Build and return AtpBlueprint object.

        Returns:
            AtpBlueprint instance
        """
        # TODO: Add validation
        return self._obj
