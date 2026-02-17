"""EOCEventRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class EOCEventRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCEventRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_module": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswImplementation,
        ),  # bswModule
        "component": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwComponent),
        ),  # component
        "event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractEvent,
        ),  # event
        "successors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EOCExecutableEntity),
        ),  # successors
    }

    def __init__(self) -> None:
        """Initialize EOCEventRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.event: Optional[AbstractEvent] = None
        self.successors: list[Any] = []


class EOCEventRefBuilder:
    """Builder for EOCEventRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCEventRef = EOCEventRef()

    def build(self) -> EOCEventRef:
        """Build and return EOCEventRef object.

        Returns:
            EOCEventRef instance
        """
        # TODO: Add validation
        return self._obj
