"""LifeCycleStateDefinitionGroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 388)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 196)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)


class LifeCycleStateDefinitionGroup(ARElement):
    """AUTOSAR LifeCycleStateDefinitionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lc_states": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LifeCycleState,
        ),  # lcStates
    }

    def __init__(self) -> None:
        """Initialize LifeCycleStateDefinitionGroup."""
        super().__init__()
        self.lc_states: list[LifeCycleState] = []


class LifeCycleStateDefinitionGroupBuilder:
    """Builder for LifeCycleStateDefinitionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleStateDefinitionGroup = LifeCycleStateDefinitionGroup()

    def build(self) -> LifeCycleStateDefinitionGroup:
        """Build and return LifeCycleStateDefinitionGroup object.

        Returns:
            LifeCycleStateDefinitionGroup instance
        """
        # TODO: Add validation
        return self._obj
