"""DdsDestinationOrder AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_destination_order import (
    DdsDestinationOrder,
)


class DdsDestinationOrder(ARObject):
    """AUTOSAR DdsDestinationOrder."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination", None, False, False, DdsDestinationOrder),  # destination
    ]

    def __init__(self) -> None:
        """Initialize DdsDestinationOrder."""
        super().__init__()
        self.destination: Optional[DdsDestinationOrder] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsDestinationOrder to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDestinationOrder":
        """Create DdsDestinationOrder from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsDestinationOrder instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsDestinationOrder since parent returns ARObject
        return cast("DdsDestinationOrder", obj)


class DdsDestinationOrderBuilder:
    """Builder for DdsDestinationOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDestinationOrder = DdsDestinationOrder()

    def build(self) -> DdsDestinationOrder:
        """Build and return DdsDestinationOrder object.

        Returns:
            DdsDestinationOrder instance
        """
        # TODO: Add validation
        return self._obj
