"""LifeCycleInfoSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 391)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_lc_state": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LifeCycleState,
        ),  # defaultLcState
        "default_period": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LifeCyclePeriod,
        ),  # defaultPeriod
        "life_cycle_infos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LifeCycleInfo,
        ),  # lifeCycleInfos
        "used_life_cycle": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LifeCycleStateDefinitionGroup,
        ),  # usedLifeCycle
    }

    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state: LifeCycleState = None
        self.default_period: Optional[LifeCyclePeriod] = None
        self.life_cycle_infos: list[LifeCycleInfo] = []
        self.used_life_cycle: LifeCycleStateDefinitionGroup = None


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
