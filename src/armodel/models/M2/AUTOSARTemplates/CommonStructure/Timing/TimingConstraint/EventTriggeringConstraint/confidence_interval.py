"""ConfidenceInterval AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ConfidenceInterval(ARObject):
    """AUTOSAR ConfidenceInterval."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lower_bound": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # lowerBound
        "propability": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # propability
        "upper_bound": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # upperBound
    }

    def __init__(self) -> None:
        """Initialize ConfidenceInterval."""
        super().__init__()
        self.lower_bound: Optional[MultidimensionalTime] = None
        self.propability: Optional[Float] = None
        self.upper_bound: Optional[MultidimensionalTime] = None


class ConfidenceIntervalBuilder:
    """Builder for ConfidenceInterval."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConfidenceInterval = ConfidenceInterval()

    def build(self) -> ConfidenceInterval:
        """Build and return ConfidenceInterval object.

        Returns:
            ConfidenceInterval instance
        """
        # TODO: Add validation
        return self._obj
