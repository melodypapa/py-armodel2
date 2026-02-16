"""BswInternalTriggeringPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class BswInternalTriggeringPoint(Identifiable):
    """AUTOSAR BswInternalTriggeringPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_impl_policy_enum", None, False, False, SwImplPolicyEnum),  # swImplPolicyEnum
    ]

    def __init__(self) -> None:
        """Initialize BswInternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswInternalTriggeringPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalTriggeringPoint":
        """Create BswInternalTriggeringPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswInternalTriggeringPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswInternalTriggeringPoint since parent returns ARObject
        return cast("BswInternalTriggeringPoint", obj)


class BswInternalTriggeringPointBuilder:
    """Builder for BswInternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggeringPoint = BswInternalTriggeringPoint()

    def build(self) -> BswInternalTriggeringPoint:
        """Build and return BswInternalTriggeringPoint object.

        Returns:
            BswInternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
