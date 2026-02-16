"""TDEventSwc AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventSwc(TimingDescriptionEvent):
    """AUTOSAR TDEventSwc."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "component": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwComponent),
        ),  # component
    }

    def __init__(self) -> None:
        """Initialize TDEventSwc."""
        super().__init__()
        self.component: Optional[Any] = None


class TDEventSwcBuilder:
    """Builder for TDEventSwc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwc = TDEventSwc()

    def build(self) -> TDEventSwc:
        """Build and return TDEventSwc object.

        Returns:
            TDEventSwc instance
        """
        # TODO: Add validation
        return self._obj
