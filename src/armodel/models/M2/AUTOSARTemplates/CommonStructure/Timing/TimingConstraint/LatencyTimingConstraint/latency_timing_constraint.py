"""LatencyTimingConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class LatencyTimingConstraint(TimingConstraint):
    """AUTOSAR LatencyTimingConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("latency", None, False, False, LatencyConstraintTypeEnum),  # latency
        ("maximum", None, False, False, MultidimensionalTime),  # maximum
        ("minimum", None, False, False, MultidimensionalTime),  # minimum
        ("nominal", None, False, False, MultidimensionalTime),  # nominal
        ("scope", None, False, False, TimingDescriptionEvent),  # scope
    ]

    def __init__(self) -> None:
        """Initialize LatencyTimingConstraint."""
        super().__init__()
        self.latency: Optional[LatencyConstraintTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.nominal: Optional[MultidimensionalTime] = None
        self.scope: Optional[TimingDescriptionEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LatencyTimingConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LatencyTimingConstraint":
        """Create LatencyTimingConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LatencyTimingConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LatencyTimingConstraint since parent returns ARObject
        return cast("LatencyTimingConstraint", obj)


class LatencyTimingConstraintBuilder:
    """Builder for LatencyTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LatencyTimingConstraint = LatencyTimingConstraint()

    def build(self) -> LatencyTimingConstraint:
        """Build and return LatencyTimingConstraint object.

        Returns:
            LatencyTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
