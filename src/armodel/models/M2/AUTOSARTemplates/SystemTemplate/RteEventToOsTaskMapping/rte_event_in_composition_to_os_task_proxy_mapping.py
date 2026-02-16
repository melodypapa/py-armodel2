"""RteEventInCompositionToOsTaskProxyMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionToOsTaskProxyMapping(Identifiable):
    """AUTOSAR RteEventInCompositionToOsTaskProxyMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("offset", None, True, False, None),  # offset
        ("os_task_proxy", None, False, False, OsTaskProxy),  # osTaskProxy
        ("rte_event_instance_ref", None, False, False, RTEEvent),  # rteEventInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize RteEventInCompositionToOsTaskProxyMapping."""
        super().__init__()
        self.offset: Optional[PositiveInteger] = None
        self.os_task_proxy: Optional[OsTaskProxy] = None
        self.rte_event_instance_ref: Optional[RTEEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RteEventInCompositionToOsTaskProxyMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInCompositionToOsTaskProxyMapping":
        """Create RteEventInCompositionToOsTaskProxyMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RteEventInCompositionToOsTaskProxyMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RteEventInCompositionToOsTaskProxyMapping since parent returns ARObject
        return cast("RteEventInCompositionToOsTaskProxyMapping", obj)


class RteEventInCompositionToOsTaskProxyMappingBuilder:
    """Builder for RteEventInCompositionToOsTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInCompositionToOsTaskProxyMapping = RteEventInCompositionToOsTaskProxyMapping()

    def build(self) -> RteEventInCompositionToOsTaskProxyMapping:
        """Build and return RteEventInCompositionToOsTaskProxyMapping object.

        Returns:
            RteEventInCompositionToOsTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
