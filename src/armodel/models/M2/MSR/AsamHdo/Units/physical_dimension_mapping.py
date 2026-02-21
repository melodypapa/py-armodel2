"""PhysicalDimensionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    first_physical_ref: Optional[ARRef]
    second_physical_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PhysicalDimensionMapping."""
        super().__init__()
        self.first_physical_ref: Optional[ARRef] = None
        self.second_physical_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimensionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalDimensionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_physical_ref
        if self.first_physical_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_physical_ref, "PhysicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-PHYSICAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_physical_ref
        if self.second_physical_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_physical_ref, "PhysicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-PHYSICAL-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimensionMapping, cls).deserialize(element)

        # Parse first_physical_ref
        child = SerializationHelper.find_child_element(element, "FIRST-PHYSICAL-REF")
        if child is not None:
            first_physical_ref_value = ARRef.deserialize(child)
            obj.first_physical_ref = first_physical_ref_value

        # Parse second_physical_ref
        child = SerializationHelper.find_child_element(element, "SECOND-PHYSICAL-REF")
        if child is not None:
            second_physical_ref_value = ARRef.deserialize(child)
            obj.second_physical_ref = second_physical_ref_value

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
