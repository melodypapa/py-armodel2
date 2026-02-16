"""TimingCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)


class TimingCondition(Identifiable):
    """AUTOSAR TimingCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("timing_condition", None, False, False, TimingCondition),  # timingCondition
    ]

    def __init__(self) -> None:
        """Initialize TimingCondition."""
        super().__init__()
        self.timing_condition: Optional[TimingCondition] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingCondition":
        """Create TimingCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingCondition since parent returns ARObject
        return cast("TimingCondition", obj)


class TimingConditionBuilder:
    """Builder for TimingCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingCondition = TimingCondition()

    def build(self) -> TimingCondition:
        """Build and return TimingCondition object.

        Returns:
            TimingCondition instance
        """
        # TODO: Add validation
        return self._obj
