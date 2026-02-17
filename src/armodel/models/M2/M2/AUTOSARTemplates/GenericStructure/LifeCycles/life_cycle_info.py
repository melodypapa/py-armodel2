"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lc_object": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Referrable,
        ),  # lcObject
        "lc_state": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LifeCycleState,
        ),  # lcState
        "period_begin": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LifeCyclePeriod,
        ),  # periodBegin
        "period_end": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LifeCyclePeriod,
        ),  # periodEnd
        "remark": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # remark
        "use_insteads": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Referrable,
        ),  # useInsteads
    }

    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object: Referrable = None
        self.lc_state: Optional[LifeCycleState] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_insteads: list[Referrable] = []


class LifeCycleInfoBuilder:
    """Builder for LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfo = LifeCycleInfo()

    def build(self) -> LifeCycleInfo:
        """Build and return LifeCycleInfo object.

        Returns:
            LifeCycleInfo instance
        """
        # TODO: Add validation
        return self._obj
