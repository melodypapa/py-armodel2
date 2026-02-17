"""TimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)


class TimingConstraint(Traceable):
    """AUTOSAR TimingConstraint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timing_condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingCondition,
        ),  # timingCondition
    }

    def __init__(self) -> None:
        """Initialize TimingConstraint."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None


class TimingConstraintBuilder:
    """Builder for TimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingConstraint = TimingConstraint()

    def build(self) -> TimingConstraint:
        """Build and return TimingConstraint object.

        Returns:
            TimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
