"""EOCExecutableEntityRefGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    let_data_exchange: Optional[LetDataExchangeParadigmEnum]
    let_intervals: list[TimingDescriptionEvent]
    max_cycle: Optional[PositiveInteger]
    max_cycles: Optional[Integer]
    max_slots: Optional[Integer]
    max_slots_per: Optional[PositiveInteger]
    nested_elements: list[Any]
    successors: list[Any]
    triggering_event: Optional[TimingDescriptionEvent]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefGroup":
        """Deserialize XML element to EOCExecutableEntityRefGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefGroup, cls).deserialize(element)

        # Parse let_data_exchange
        child = ARObject._find_child_element(element, "LET-DATA-EXCHANGE")
        if child is not None:
            let_data_exchange_value = LetDataExchangeParadigmEnum.deserialize(child)
            obj.let_data_exchange = let_data_exchange_value

        # Parse let_intervals (list from container "LET-INTERVALS")
        obj.let_intervals = []
        container = ARObject._find_child_element(element, "LET-INTERVALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.let_intervals.append(child_value)

        # Parse max_cycle
        child = ARObject._find_child_element(element, "MAX-CYCLE")
        if child is not None:
            max_cycle_value = child.text
            obj.max_cycle = max_cycle_value

        # Parse max_cycles
        child = ARObject._find_child_element(element, "MAX-CYCLES")
        if child is not None:
            max_cycles_value = child.text
            obj.max_cycles = max_cycles_value

        # Parse max_slots
        child = ARObject._find_child_element(element, "MAX-SLOTS")
        if child is not None:
            max_slots_value = child.text
            obj.max_slots = max_slots_value

        # Parse max_slots_per
        child = ARObject._find_child_element(element, "MAX-SLOTS-PER")
        if child is not None:
            max_slots_per_value = child.text
            obj.max_slots_per = max_slots_per_value

        # Parse nested_elements (list from container "NESTED-ELEMENTS")
        obj.nested_elements = []
        container = ARObject._find_child_element(element, "NESTED-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nested_elements.append(child_value)

        # Parse successors (list from container "SUCCESSORS")
        obj.successors = []
        container = ARObject._find_child_element(element, "SUCCESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.successors.append(child_value)

        # Parse triggering_event
        child = ARObject._find_child_element(element, "TRIGGERING-EVENT")
        if child is not None:
            triggering_event_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.triggering_event = triggering_event_value

        return obj



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
