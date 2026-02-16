"""ComMgrUserNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class ComMgrUserNeeds(ServiceNeeds):
    """AUTOSAR ComMgrUserNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_comm_mode_enum", None, False, False, MaxCommModeEnum),  # maxCommModeEnum
    ]

    def __init__(self) -> None:
        """Initialize ComMgrUserNeeds."""
        super().__init__()
        self.max_comm_mode_enum: Optional[MaxCommModeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ComMgrUserNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComMgrUserNeeds":
        """Create ComMgrUserNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ComMgrUserNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ComMgrUserNeeds since parent returns ARObject
        return cast("ComMgrUserNeeds", obj)


class ComMgrUserNeedsBuilder:
    """Builder for ComMgrUserNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComMgrUserNeeds = ComMgrUserNeeds()

    def build(self) -> ComMgrUserNeeds:
        """Build and return ComMgrUserNeeds object.

        Returns:
            ComMgrUserNeeds instance
        """
        # TODO: Add validation
        return self._obj
