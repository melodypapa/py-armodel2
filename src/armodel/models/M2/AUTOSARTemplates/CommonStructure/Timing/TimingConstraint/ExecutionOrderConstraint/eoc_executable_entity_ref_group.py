"""EOCExecutableEntityRefGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("let_data_exchange", None, False, False, LetDataExchangeParadigmEnum),  # letDataExchange
        ("let_intervals", None, False, True, TimingDescriptionEvent),  # letIntervals
        ("max_cycle", None, True, False, None),  # maxCycle
        ("max_cycles", None, True, False, None),  # maxCycles
        ("max_slots", None, True, False, None),  # maxSlots
        ("max_slots_per", None, True, False, None),  # maxSlotsPer
        ("nested_elements", None, False, True, any (EOCExecutableEntity)),  # nestedElements
        ("successors", None, False, True, any (EOCExecutableEntity)),  # successors
        ("triggering_event", None, False, False, TimingDescriptionEvent),  # triggeringEvent
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EOCExecutableEntityRefGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefGroup":
        """Create EOCExecutableEntityRefGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EOCExecutableEntityRefGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EOCExecutableEntityRefGroup since parent returns ARObject
        return cast("EOCExecutableEntityRefGroup", obj)


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
