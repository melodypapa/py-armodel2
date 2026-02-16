"""SynchronizationPointConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("source_eecs", None, False, True, any (EOCExecutableEntity)),  # sourceEecs
        ("source_events", None, False, True, AbstractEvent),  # sourceEvents
        ("target_eecs", None, False, True, any (EOCExecutableEntity)),  # targetEecs
        ("target_events", None, False, True, AbstractEvent),  # targetEvents
    ]

    def __init__(self) -> None:
        """Initialize SynchronizationPointConstraint."""
        super().__init__()
        self.source_eecs: list[Any] = []
        self.source_events: list[AbstractEvent] = []
        self.target_eecs: list[Any] = []
        self.target_events: list[AbstractEvent] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SynchronizationPointConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationPointConstraint":
        """Create SynchronizationPointConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SynchronizationPointConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SynchronizationPointConstraint since parent returns ARObject
        return cast("SynchronizationPointConstraint", obj)


class SynchronizationPointConstraintBuilder:
    """Builder for SynchronizationPointConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()

    def build(self) -> SynchronizationPointConstraint:
        """Build and return SynchronizationPointConstraint object.

        Returns:
            SynchronizationPointConstraint instance
        """
        # TODO: Add validation
        return self._obj
