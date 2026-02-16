"""InstantiationRTEEventProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class InstantiationRTEEventProps(ARObject):
    """AUTOSAR InstantiationRTEEventProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("refined_event", None, False, False, RTEEvent),  # refinedEvent
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize InstantiationRTEEventProps."""
        super().__init__()
        self.refined_event: Optional[RTEEvent] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InstantiationRTEEventProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationRTEEventProps":
        """Create InstantiationRTEEventProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InstantiationRTEEventProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InstantiationRTEEventProps since parent returns ARObject
        return cast("InstantiationRTEEventProps", obj)


class InstantiationRTEEventPropsBuilder:
    """Builder for InstantiationRTEEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationRTEEventProps = InstantiationRTEEventProps()

    def build(self) -> InstantiationRTEEventProps:
        """Build and return InstantiationRTEEventProps object.

        Returns:
            InstantiationRTEEventProps instance
        """
        # TODO: Add validation
        return self._obj
