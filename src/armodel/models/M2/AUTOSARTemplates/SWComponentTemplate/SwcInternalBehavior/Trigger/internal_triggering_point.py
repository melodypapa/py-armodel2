"""InternalTriggeringPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    """AUTOSAR InternalTriggeringPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_impl_policy_enum", None, False, False, SwImplPolicyEnum),  # swImplPolicyEnum
    ]

    def __init__(self) -> None:
        """Initialize InternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InternalTriggeringPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalTriggeringPoint":
        """Create InternalTriggeringPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InternalTriggeringPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InternalTriggeringPoint since parent returns ARObject
        return cast("InternalTriggeringPoint", obj)


class InternalTriggeringPointBuilder:
    """Builder for InternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggeringPoint = InternalTriggeringPoint()

    def build(self) -> InternalTriggeringPoint:
        """Build and return InternalTriggeringPoint object.

        Returns:
            InternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
