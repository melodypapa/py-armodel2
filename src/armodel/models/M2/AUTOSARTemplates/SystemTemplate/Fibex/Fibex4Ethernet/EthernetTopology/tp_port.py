"""TpPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize dynamically
        if self.dynamically is not None:
            serialized = ARObject._serialize_item(self.dynamically, "Boolean")
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
            serialized = ARObject._serialize_item(self.port_number, "PositiveInteger")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dynamically
        child = ARObject._find_child_element(element, "DYNAMICALLY")
        if child is not None:
            dynamically_value = child.text
            obj.dynamically = dynamically_value

        # Parse port_number
        child = ARObject._find_child_element(element, "PORT-NUMBER")
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
