"""TDEventCycleStart AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDEventCycleStart(TDEventCom):
    """AUTOSAR TDEventCycleStart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cycle_repetition": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cycleRepetition
    }

    def __init__(self) -> None:
        """Initialize TDEventCycleStart."""
        super().__init__()
        self.cycle_repetition: Optional[Integer] = None


class TDEventCycleStartBuilder:
    """Builder for TDEventCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCycleStart = TDEventCycleStart()

    def build(self) -> TDEventCycleStart:
        """Build and return TDEventCycleStart object.

        Returns:
            TDEventCycleStart instance
        """
        # TODO: Add validation
        return self._obj
