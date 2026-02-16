"""InstantiationTimingEventProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """AUTOSAR InstantiationTimingEventProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("period", None, True, False, None),  # period
    ]

    def __init__(self) -> None:
        """Initialize InstantiationTimingEventProps."""
        super().__init__()
        self.period: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InstantiationTimingEventProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationTimingEventProps":
        """Create InstantiationTimingEventProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InstantiationTimingEventProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InstantiationTimingEventProps since parent returns ARObject
        return cast("InstantiationTimingEventProps", obj)


class InstantiationTimingEventPropsBuilder:
    """Builder for InstantiationTimingEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationTimingEventProps = InstantiationTimingEventProps()

    def build(self) -> InstantiationTimingEventProps:
        """Build and return InstantiationTimingEventProps object.

        Returns:
            InstantiationTimingEventProps instance
        """
        # TODO: Add validation
        return self._obj
