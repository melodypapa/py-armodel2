"""TimingConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timing_condition", None, False, False, TimingCondition),  # timingCondition
    ]

    def __init__(self) -> None:
        """Initialize TimingConstraint."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingConstraint":
        """Create TimingConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingConstraint since parent returns ARObject
        return cast("TimingConstraint", obj)


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
