"""TDEventVfb AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventVfb(TimingDescriptionEvent):
    """AUTOSAR TDEventVfb."""
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
        """Initialize TDEventVfb."""
        super().__init__()
        self.component: Optional[Any] = None


class TDEventVfbBuilder:
    """Builder for TDEventVfb."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfb = TDEventVfb()

    def build(self) -> TDEventVfb:
        """Build and return TDEventVfb object.

        Returns:
            TDEventVfb instance
        """
        # TODO: Add validation
        return self._obj
