"""LifeCycleStateDefinitionGroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 388)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 196)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)


class LifeCycleStateDefinitionGroup(ARElement):
    """AUTOSAR LifeCycleStateDefinitionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lc_states: list[LifeCycleState]
    def __init__(self) -> None:
        """Initialize LifeCycleStateDefinitionGroup."""
        super().__init__()
        self.lc_states: list[LifeCycleState] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleStateDefinitionGroup":
        """Deserialize XML element to LifeCycleStateDefinitionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleStateDefinitionGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lc_states (list)
        obj.lc_states = []
        for child in ARObject._find_all_child_elements(element, "LC-STATES"):
            lc_states_value = ARObject._deserialize_by_tag(child, "LifeCycleState")
            obj.lc_states.append(lc_states_value)

        return obj



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
