"""OrderedMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class OrderedMaster(ARObject):
    """AUTOSAR OrderedMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("index", None, True, False, None),  # index
        ("time_sync_server_configuration", None, False, False, TimeSyncServerConfiguration),  # timeSyncServerConfiguration
    ]

    def __init__(self) -> None:
        """Initialize OrderedMaster."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert OrderedMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OrderedMaster":
        """Create OrderedMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            OrderedMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to OrderedMaster since parent returns ARObject
        return cast("OrderedMaster", obj)


class OrderedMasterBuilder:
    """Builder for OrderedMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OrderedMaster = OrderedMaster()

    def build(self) -> OrderedMaster:
        """Build and return OrderedMaster object.

        Returns:
            OrderedMaster instance
        """
        # TODO: Add validation
        return self._obj
