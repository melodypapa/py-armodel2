"""RteEventInCompositionSeparation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionSeparation(Identifiable):
    """AUTOSAR RteEventInCompositionSeparation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rte_event_instance_refs", None, False, True, RTEEvent),  # rteEventInstanceRefs
    ]

    def __init__(self) -> None:
        """Initialize RteEventInCompositionSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RteEventInCompositionSeparation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInCompositionSeparation":
        """Create RteEventInCompositionSeparation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RteEventInCompositionSeparation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RteEventInCompositionSeparation since parent returns ARObject
        return cast("RteEventInCompositionSeparation", obj)


class RteEventInCompositionSeparationBuilder:
    """Builder for RteEventInCompositionSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInCompositionSeparation = RteEventInCompositionSeparation()

    def build(self) -> RteEventInCompositionSeparation:
        """Build and return RteEventInCompositionSeparation object.

        Returns:
            RteEventInCompositionSeparation instance
        """
        # TODO: Add validation
        return self._obj
