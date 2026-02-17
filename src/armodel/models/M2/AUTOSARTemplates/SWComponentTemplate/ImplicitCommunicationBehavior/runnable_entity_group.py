"""RunnableEntityGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 222)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RunnableEntityGroup(Identifiable):
    """AUTOSAR RunnableEntityGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "runnable_entities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RunnableEntity,
        ),  # runnableEntities
        "runnable_entity_group_group_in_composition_instance_refs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="RunnableEntityGroup",
        ),  # runnableEntityGroupGroupInCompositionInstanceRefs
    }

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
