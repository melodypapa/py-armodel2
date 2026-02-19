"""LifeCycleInfoSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 391)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
    LifeCycleInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
    LifeCycleStateDefinitionGroup,
)


class LifeCycleInfoSet(ARElement):
    """AUTOSAR LifeCycleInfoSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_lc_state: LifeCycleState
    default_period: Optional[LifeCyclePeriod]
    life_cycle_infos: list[LifeCycleInfo]
    used_life_cycle: LifeCycleStateDefinitionGroup
    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state: LifeCycleState = None
        self.default_period: Optional[LifeCyclePeriod] = None
        self.life_cycle_infos: list[LifeCycleInfo] = []
        self.used_life_cycle: LifeCycleStateDefinitionGroup = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfoSet":
        """Deserialize XML element to LifeCycleInfoSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfoSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_lc_state
        child = ARObject._find_child_element(element, "DEFAULT-LC-STATE")
        if child is not None:
            default_lc_state_value = ARObject._deserialize_by_tag(child, "LifeCycleState")
            obj.default_lc_state = default_lc_state_value

        # Parse default_period
        child = ARObject._find_child_element(element, "DEFAULT-PERIOD")
        if child is not None:
            default_period_value = ARObject._deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period = default_period_value

        # Parse life_cycle_infos (list)
        obj.life_cycle_infos = []
        for child in ARObject._find_all_child_elements(element, "LIFE-CYCLE-INFOS"):
            life_cycle_infos_value = ARObject._deserialize_by_tag(child, "LifeCycleInfo")
            obj.life_cycle_infos.append(life_cycle_infos_value)

        # Parse used_life_cycle
        child = ARObject._find_child_element(element, "USED-LIFE-CYCLE")
        if child is not None:
            used_life_cycle_value = ARObject._deserialize_by_tag(child, "LifeCycleStateDefinitionGroup")
            obj.used_life_cycle = used_life_cycle_value

        return obj



class LifeCycleInfoSetBuilder:
    """Builder for LifeCycleInfoSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfoSet = LifeCycleInfoSet()

    def build(self) -> LifeCycleInfoSet:
        """Build and return LifeCycleInfoSet object.

        Returns:
            LifeCycleInfoSet instance
        """
        # TODO: Add validation
        return self._obj
