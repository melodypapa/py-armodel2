"""Ieee1722TpEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 579)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722TpEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR Ieee1722TpEthernetFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    relative: Optional[TimeValue]
    stream_identifier: Optional[PositiveInteger]
    sub_type: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ieee1722TpEthernetFrame."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize Ieee1722TpEthernetFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ieee1722TpEthernetFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize relative
        if self.relative is not None:
            serialized = ARObject._serialize_item(self.relative, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stream_identifier
        if self.stream_identifier is not None:
            serialized = ARObject._serialize_item(self.stream_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_type
        if self.sub_type is not None:
            serialized = ARObject._serialize_item(self.sub_type, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version
        if self.version is not None:
            serialized = ARObject._serialize_item(self.version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ieee1722TpEthernetFrame":
        """Deserialize XML element to Ieee1722TpEthernetFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ieee1722TpEthernetFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ieee1722TpEthernetFrame, cls).deserialize(element)

        # Parse relative
        child = ARObject._find_child_element(element, "RELATIVE")
        if child is not None:
            relative_value = child.text
            obj.relative = relative_value

        # Parse stream_identifier
        child = ARObject._find_child_element(element, "STREAM-IDENTIFIER")
        if child is not None:
            stream_identifier_value = child.text
            obj.stream_identifier = stream_identifier_value

        # Parse sub_type
        child = ARObject._find_child_element(element, "SUB-TYPE")
        if child is not None:
            sub_type_value = child.text
            obj.sub_type = sub_type_value

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        return obj



class Ieee1722TpEthernetFrameBuilder:
    """Builder for Ieee1722TpEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722TpEthernetFrame = Ieee1722TpEthernetFrame()

    def build(self) -> Ieee1722TpEthernetFrame:
        """Build and return Ieee1722TpEthernetFrame object.

        Returns:
            Ieee1722TpEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
