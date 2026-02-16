"""SystemTiming AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class SystemTiming(TimingExtension):
    """AUTOSAR SystemTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "system": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # system
    }

    def __init__(self) -> None:
        """Initialize SystemTiming."""
        super().__init__()
        self.system: Optional[System] = None


class SystemTimingBuilder:
    """Builder for SystemTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemTiming = SystemTiming()

    def build(self) -> SystemTiming:
        """Build and return SystemTiming object.

        Returns:
            SystemTiming instance
        """
        # TODO: Add validation
        return self._obj
