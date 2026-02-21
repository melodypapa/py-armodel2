"""BusMirrorChannelMappingIp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 705)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingIp(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingIp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transmission: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingIp."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannelMappingIp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannelMappingIp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize transmission
        if self.transmission is not None:
            serialized = ARObject._serialize_item(self.transmission, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingIp":
        """Deserialize XML element to BusMirrorChannelMappingIp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMappingIp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMappingIp, cls).deserialize(element)

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class BusMirrorChannelMappingIpBuilder:
    """Builder for BusMirrorChannelMappingIp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingIp = BusMirrorChannelMappingIp()

    def build(self) -> BusMirrorChannelMappingIp:
        """Build and return BusMirrorChannelMappingIp object.

        Returns:
            BusMirrorChannelMappingIp instance
        """
        # TODO: Add validation
        return self._obj
