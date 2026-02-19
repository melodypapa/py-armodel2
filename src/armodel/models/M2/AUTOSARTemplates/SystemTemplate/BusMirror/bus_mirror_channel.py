"""BusMirrorChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 698)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class BusMirrorChannel(ARObject):
    """AUTOSAR BusMirrorChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bus_mirror: Optional[PositiveInteger]
    channel: Optional[PhysicalChannel]
    def __init__(self) -> None:
        """Initialize BusMirrorChannel."""
        super().__init__()
        self.bus_mirror: Optional[PositiveInteger] = None
        self.channel: Optional[PhysicalChannel] = None
    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bus_mirror
        if self.bus_mirror is not None:
            serialized = ARObject._serialize_item(self.bus_mirror, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-MIRROR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize channel
        if self.channel is not None:
            serialized = ARObject._serialize_item(self.channel, "PhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannel":
        """Deserialize XML element to BusMirrorChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bus_mirror
        child = ARObject._find_child_element(element, "BUS-MIRROR")
        if child is not None:
            bus_mirror_value = child.text
            obj.bus_mirror = bus_mirror_value

        # Parse channel
        child = ARObject._find_child_element(element, "CHANNEL")
        if child is not None:
            channel_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.channel = channel_value

        return obj



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
