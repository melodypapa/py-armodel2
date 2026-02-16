"""InstanceEventInCompositionInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class InstanceEventInCompositionInstanceRef(ARObject):
    """AUTOSAR InstanceEventInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("context_prototypes", None, False, True, any (SwComponent)),  # contextPrototypes
        ("target_event", None, False, False, RTEEvent),  # targetEvent
    ]

    def __init__(self) -> None:
        """Initialize InstanceEventInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_prototypes: list[Any] = []
        self.target_event: Optional[RTEEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InstanceEventInCompositionInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstanceEventInCompositionInstanceRef":
        """Create InstanceEventInCompositionInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InstanceEventInCompositionInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InstanceEventInCompositionInstanceRef since parent returns ARObject
        return cast("InstanceEventInCompositionInstanceRef", obj)


class InstanceEventInCompositionInstanceRefBuilder:
    """Builder for InstanceEventInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstanceEventInCompositionInstanceRef = InstanceEventInCompositionInstanceRef()

    def build(self) -> InstanceEventInCompositionInstanceRef:
        """Build and return InstanceEventInCompositionInstanceRef object.

        Returns:
            InstanceEventInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
