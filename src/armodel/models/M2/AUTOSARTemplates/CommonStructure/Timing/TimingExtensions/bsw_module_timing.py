"""BswModuleTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)


class BswModuleTiming(TimingExtension):
    """AUTOSAR BswModuleTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswInternalBehavior,
        ),  # behavior
    }

    def __init__(self) -> None:
        """Initialize BswModuleTiming."""
        super().__init__()
        self.behavior: Optional[BswInternalBehavior] = None


class BswModuleTimingBuilder:
    """Builder for BswModuleTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleTiming = BswModuleTiming()

    def build(self) -> BswModuleTiming:
        """Build and return BswModuleTiming object.

        Returns:
            BswModuleTiming instance
        """
        # TODO: Add validation
        return self._obj
