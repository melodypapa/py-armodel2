"""SwcTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 25)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcTiming(TimingExtension):
    """AUTOSAR SwcTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwcInternalBehavior,
        ),  # behavior
    }

    def __init__(self) -> None:
        """Initialize SwcTiming."""
        super().__init__()
        self.behavior: Optional[SwcInternalBehavior] = None


class SwcTimingBuilder:
    """Builder for SwcTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcTiming = SwcTiming()

    def build(self) -> SwcTiming:
        """Build and return SwcTiming object.

        Returns:
            SwcTiming instance
        """
        # TODO: Add validation
        return self._obj
