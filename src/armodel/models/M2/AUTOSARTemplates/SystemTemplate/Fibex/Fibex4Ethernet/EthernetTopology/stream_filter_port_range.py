"""StreamFilterPortRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterPortRange(ARObject):
    """AUTOSAR StreamFilterPortRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max: Optional[PositiveInteger]
    min: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize StreamFilterPortRange."""
        super().__init__()
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterPortRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize max
        if self.max is not None:
            serialized = ARObject._serialize_item(self.max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = ARObject._serialize_item(self.min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterPortRange":
        """Deserialize XML element to StreamFilterPortRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterPortRange object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class StreamFilterPortRangeBuilder:
    """Builder for StreamFilterPortRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterPortRange = StreamFilterPortRange()

    def build(self) -> StreamFilterPortRange:
        """Build and return StreamFilterPortRange object.

        Returns:
            StreamFilterPortRange instance
        """
        # TODO: Add validation
        return self._obj
