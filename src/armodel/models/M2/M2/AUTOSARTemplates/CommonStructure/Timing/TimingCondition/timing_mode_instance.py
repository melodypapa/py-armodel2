"""TimingModeInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class TimingModeInstance(Identifiable):
    """AUTOSAR TimingModeInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # modeInstance
    }

    def __init__(self) -> None:
        """Initialize TimingModeInstance."""
        super().__init__()
        self.mode_instance: Optional[Any] = None


class TimingModeInstanceBuilder:
    """Builder for TimingModeInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingModeInstance = TimingModeInstance()

    def build(self) -> TimingModeInstance:
        """Build and return TimingModeInstance object.

        Returns:
            TimingModeInstance instance
        """
        # TODO: Add validation
        return self._obj
