"""ConsistencyNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 221)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 178)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class ConsistencyNeeds(Identifiable):
    """AUTOSAR ConsistencyNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dpg_does_nots: list[DataPrototypeGroup]
    dpg_requireses: list[DataPrototypeGroup]
    reg_does_nots: list[RunnableEntityGroup]
    reg_requireses: list[RunnableEntityGroup]
    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_nots: list[DataPrototypeGroup] = []
        self.dpg_requireses: list[DataPrototypeGroup] = []
        self.reg_does_nots: list[RunnableEntityGroup] = []
        self.reg_requireses: list[RunnableEntityGroup] = []


class ConsistencyNeedsBuilder:
    """Builder for ConsistencyNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsistencyNeeds = ConsistencyNeeds()

    def build(self) -> ConsistencyNeeds:
        """Build and return ConsistencyNeeds object.

        Returns:
            ConsistencyNeeds instance
        """
        # TODO: Add validation
        return self._obj
