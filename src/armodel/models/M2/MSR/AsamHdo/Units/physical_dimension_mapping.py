"""PhysicalDimensionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)


class PhysicalDimensionMapping(ARObject):
    """AUTOSAR PhysicalDimensionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_physical: Optional[PhysicalDimension]
    second_physical: Optional[PhysicalDimension]
    def __init__(self) -> None:
        """Initialize PhysicalDimensionMapping."""
        super().__init__()
        self.first_physical: Optional[PhysicalDimension] = None
        self.second_physical: Optional[PhysicalDimension] = None
    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimensionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize first_physical
        if self.first_physical is not None:
            serialized = ARObject._serialize_item(self.first_physical, "PhysicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-PHYSICAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_physical
        if self.second_physical is not None:
            serialized = ARObject._serialize_item(self.second_physical, "PhysicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-PHYSICAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMapping":
        """Deserialize XML element to PhysicalDimensionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimensionMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_physical
        child = ARObject._find_child_element(element, "FIRST-PHYSICAL")
        if child is not None:
            first_physical_value = ARObject._deserialize_by_tag(child, "PhysicalDimension")
            obj.first_physical = first_physical_value

        # Parse second_physical
        child = ARObject._find_child_element(element, "SECOND-PHYSICAL")
        if child is not None:
            second_physical_value = ARObject._deserialize_by_tag(child, "PhysicalDimension")
            obj.second_physical = second_physical_value

        return obj



class PhysicalDimensionMappingBuilder:
    """Builder for PhysicalDimensionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimensionMapping = PhysicalDimensionMapping()

    def build(self) -> PhysicalDimensionMapping:
        """Build and return PhysicalDimensionMapping object.

        Returns:
            PhysicalDimensionMapping instance
        """
        # TODO: Add validation
        return self._obj
