"""BswCompositionTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class BswCompositionTiming(TimingExtension):
    """AUTOSAR BswCompositionTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "implementations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswImplementation,
        ),  # implementations
    }

    def __init__(self) -> None:
        """Initialize BswCompositionTiming."""
        super().__init__()
        self.implementations: list[BswImplementation] = []


class BswCompositionTimingBuilder:
    """Builder for BswCompositionTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCompositionTiming = BswCompositionTiming()

    def build(self) -> BswCompositionTiming:
        """Build and return BswCompositionTiming object.

        Returns:
            BswCompositionTiming instance
        """
        # TODO: Add validation
        return self._obj
