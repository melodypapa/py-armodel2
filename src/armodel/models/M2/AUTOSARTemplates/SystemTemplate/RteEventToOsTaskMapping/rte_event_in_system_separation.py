"""RteEventInSystemSeparation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInSystemSeparation(Identifiable):
    """AUTOSAR RteEventInSystemSeparation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rte_event_instance_refs", None, False, True, RTEEvent),  # rteEventInstanceRefs
    ]

    def __init__(self) -> None:
        """Initialize RteEventInSystemSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RteEventInSystemSeparation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInSystemSeparation":
        """Create RteEventInSystemSeparation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RteEventInSystemSeparation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RteEventInSystemSeparation since parent returns ARObject
        return cast("RteEventInSystemSeparation", obj)


class RteEventInSystemSeparationBuilder:
    """Builder for RteEventInSystemSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInSystemSeparation = RteEventInSystemSeparation()

    def build(self) -> RteEventInSystemSeparation:
        """Build and return RteEventInSystemSeparation object.

        Returns:
            RteEventInSystemSeparation instance
        """
        # TODO: Add validation
        return self._obj
