"""EOCExecutableEntityRefGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRefGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "let_data_exchange": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LetDataExchangeParadigmEnum,
        ),  # letDataExchange
        "let_intervals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingDescriptionEvent,
        ),  # letIntervals
        "max_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxCycle
        "max_cycles": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxCycles
        "max_slots": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSlots
        "max_slots_per": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSlotsPer
        "nested_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EOCExecutableEntity),
        ),  # nestedElements
        "successors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EOCExecutableEntity),
        ),  # successors
        "triggering_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescriptionEvent,
        ),  # triggeringEvent
    }

    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefGroup."""
        super().__init__()
        self.let_data_exchange: Optional[LetDataExchangeParadigmEnum] = None
        self.let_intervals: list[TimingDescriptionEvent] = []
        self.max_cycle: Optional[PositiveInteger] = None
        self.max_cycles: Optional[Integer] = None
        self.max_slots: Optional[Integer] = None
        self.max_slots_per: Optional[PositiveInteger] = None
        self.nested_elements: list[Any] = []
        self.successors: list[Any] = []
        self.triggering_event: Optional[TimingDescriptionEvent] = None


class EOCExecutableEntityRefGroupBuilder:
    """Builder for EOCExecutableEntityRefGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefGroup = EOCExecutableEntityRefGroup()

    def build(self) -> EOCExecutableEntityRefGroup:
        """Build and return EOCExecutableEntityRefGroup object.

        Returns:
            EOCExecutableEntityRefGroup instance
        """
        # TODO: Add validation
        return self._obj
