"""FlexrayPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayChannelName,
)


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    channel_name: Optional[FlexrayChannelName]
    def __init__(self) -> None:
        """Initialize FlexrayPhysicalChannel."""
        super().__init__()
        self.channel_name: Optional[FlexrayChannelName] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize channel_name
        if self.channel_name is not None:
            serialized = ARObject._serialize_item(self.channel_name, "FlexrayChannelName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayPhysicalChannel":
        """Deserialize XML element to FlexrayPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayPhysicalChannel, cls).deserialize(element)

        # Parse channel_name
        child = ARObject._find_child_element(element, "CHANNEL-NAME")
        if child is not None:
            channel_name_value = FlexrayChannelName.deserialize(child)
            obj.channel_name = channel_name_value

        return obj



class FlexrayPhysicalChannelBuilder:
    """Builder for FlexrayPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayPhysicalChannel = FlexrayPhysicalChannel()

    def build(self) -> FlexrayPhysicalChannel:
        """Build and return FlexrayPhysicalChannel object.

        Returns:
            FlexrayPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
