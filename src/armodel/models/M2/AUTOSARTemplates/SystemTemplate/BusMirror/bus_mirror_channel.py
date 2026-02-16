"""BusMirrorChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class BusMirrorChannel(ARObject):
    """AUTOSAR BusMirrorChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bus_mirror", None, True, False, None),  # busMirror
        ("channel", None, False, False, PhysicalChannel),  # channel
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorChannel."""
        super().__init__()
        self.bus_mirror: Optional[PositiveInteger] = None
        self.channel: Optional[PhysicalChannel] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannel":
        """Create BusMirrorChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorChannel since parent returns ARObject
        return cast("BusMirrorChannel", obj)


class BusMirrorChannelBuilder:
    """Builder for BusMirrorChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannel = BusMirrorChannel()

    def build(self) -> BusMirrorChannel:
        """Build and return BusMirrorChannel object.

        Returns:
            BusMirrorChannel instance
        """
        # TODO: Add validation
        return self._obj
