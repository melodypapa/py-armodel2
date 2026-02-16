"""Trigger AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class Trigger(Identifiable):
    """AUTOSAR Trigger."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_impl_policy_enum", None, False, False, SwImplPolicyEnum),  # swImplPolicyEnum
        ("trigger_period", None, False, False, MultidimensionalTime),  # triggerPeriod
    ]

    def __init__(self) -> None:
        """Initialize Trigger."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.trigger_period: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Trigger to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Trigger":
        """Create Trigger from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Trigger instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Trigger since parent returns ARObject
        return cast("Trigger", obj)


class TriggerBuilder:
    """Builder for Trigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Trigger = Trigger()

    def build(self) -> Trigger:
        """Build and return Trigger object.

        Returns:
            Trigger instance
        """
        # TODO: Add validation
        return self._obj
