"""TimingExtension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)


class TimingExtension(ARElement):
    """AUTOSAR TimingExtension."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timing_clocks": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingClock,
        ),  # timingClocks
        "timing_clock_syncs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingClockSyncAccuracy,
        ),  # timingClockSyncs
        "timing_conditions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingCondition,
        ),  # timingConditions
        "timings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingConstraint,
        ),  # timings
        "timing_resource": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingExtension,
        ),  # timingResource
    }

    def __init__(self) -> None:
        """Initialize TimingExtension."""
        super().__init__()
        self.timing_clocks: list[TimingClock] = []
        self.timing_clock_syncs: list[TimingClockSyncAccuracy] = []
        self.timing_conditions: list[TimingCondition] = []
        self.timings: list[TimingConstraint] = []
        self.timing_resource: Optional[TimingExtension] = None


class TimingExtensionBuilder:
    """Builder for TimingExtension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtension = TimingExtension()

    def build(self) -> TimingExtension:
        """Build and return TimingExtension object.

        Returns:
            TimingExtension instance
        """
        # TODO: Add validation
        return self._obj
