"""SomeipTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SomeipTpChannel(Identifiable):
    """AUTOSAR SomeipTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    burst_size: Optional[PositiveInteger]
    rx_timeout_time: Optional[TimeValue]
    separation_time: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize SomeipTpChannel."""
        super().__init__()
        self.burst_size: Optional[PositiveInteger] = None
        self.rx_timeout_time: Optional[TimeValue] = None
        self.separation_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize burst_size
        if self.burst_size is not None:
            serialized = ARObject._serialize_item(self.burst_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BURST-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_timeout_time
        if self.rx_timeout_time is not None:
            serialized = ARObject._serialize_item(self.rx_timeout_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-TIMEOUT-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize separation_time
        if self.separation_time is not None:
            serialized = ARObject._serialize_item(self.separation_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEPARATION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpChannel":
        """Deserialize XML element to SomeipTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpChannel, cls).deserialize(element)

        # Parse burst_size
        child = ARObject._find_child_element(element, "BURST-SIZE")
        if child is not None:
            burst_size_value = child.text
            obj.burst_size = burst_size_value

        # Parse rx_timeout_time
        child = ARObject._find_child_element(element, "RX-TIMEOUT-TIME")
        if child is not None:
            rx_timeout_time_value = child.text
            obj.rx_timeout_time = rx_timeout_time_value

        # Parse separation_time
        child = ARObject._find_child_element(element, "SEPARATION-TIME")
        if child is not None:
            separation_time_value = child.text
            obj.separation_time = separation_time_value

        return obj



class SomeipTpChannelBuilder:
    """Builder for SomeipTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpChannel = SomeipTpChannel()

    def build(self) -> SomeipTpChannel:
        """Build and return SomeipTpChannel object.

        Returns:
            SomeipTpChannel instance
        """
        # TODO: Add validation
        return self._obj
