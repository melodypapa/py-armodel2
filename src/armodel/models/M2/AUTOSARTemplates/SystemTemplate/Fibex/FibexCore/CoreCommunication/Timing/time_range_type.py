"""TimeRangeType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimeRangeType(ARObject):
    """AUTOSAR TimeRangeType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tolerance_tolerance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimeRangeType,
        ),  # toleranceTolerance
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize TimeRangeType."""
        super().__init__()
        self.tolerance_tolerance: Optional[TimeRangeType] = None
        self.value: Optional[TimeValue] = None


class TimeRangeTypeBuilder:
    """Builder for TimeRangeType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeRangeType = TimeRangeType()

    def build(self) -> TimeRangeType:
        """Build and return TimeRangeType object.

        Returns:
            TimeRangeType instance
        """
        # TODO: Add validation
        return self._obj
