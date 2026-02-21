"""TpPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TpPort(ARObject):
    """AUTOSAR TpPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamically: Optional[Boolean]
    port_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TpPort."""
        super().__init__()
        self.dynamically: Optional[Boolean] = None
        self.port_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize TpPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TpPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamically
        if self.dynamically is not None:
            serialized = SerializationHelper.serialize_item(self.dynamically, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMICALLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_number
        if self.port_number is not None:
            serialized = SerializationHelper.serialize_item(self.port_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpPort":
        """Deserialize XML element to TpPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TpPort, cls).deserialize(element)

        # Parse dynamically
        child = SerializationHelper.find_child_element(element, "DYNAMICALLY")
        if child is not None:
            dynamically_value = child.text
            obj.dynamically = dynamically_value

        # Parse port_number
        child = SerializationHelper.find_child_element(element, "PORT-NUMBER")
        if child is not None:
            port_number_value = child.text
            obj.port_number = port_number_value

        return obj



class TpPortBuilder:
    """Builder for TpPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpPort = TpPort()

    def build(self) -> TpPort:
        """Build and return TpPort object.

        Returns:
            TpPort instance
        """
        # TODO: Add validation
        return self._obj
