"""RunnableEntityGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 222)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RunnableEntityGroup(Identifiable):
    """AUTOSAR RunnableEntityGroup."""

    runnable_entities: list[RunnableEntity]
    runnable_entity_group_group_in_composition_instance_refs: list[RunnableEntityGroup]
    def __init__(self) -> None:
        """Initialize RunnableEntityGroup."""
        super().__init__()
        self.runnable_entities: list[RunnableEntity] = []
        self.runnable_entity_group_group_in_composition_instance_refs: list[RunnableEntityGroup] = []


class RunnableEntityGroupBuilder:
    """Builder for RunnableEntityGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityGroup = RunnableEntityGroup()

    def build(self) -> RunnableEntityGroup:
        """Build and return RunnableEntityGroup object.

        Returns:
            RunnableEntityGroup instance
        """
        # TODO: Add validation
        return self._obj
