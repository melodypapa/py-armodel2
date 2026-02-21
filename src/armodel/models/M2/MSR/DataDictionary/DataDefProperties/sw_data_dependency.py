"""SwDataDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 373)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_generic_math import (
    CompuGenericMath,
)


class SwDataDependency(ARObject):
    """AUTOSAR SwDataDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_data: Optional[CompuGenericMath]
    def __init__(self) -> None:
        """Initialize SwDataDependency."""
        super().__init__()
        self.sw_data: Optional[CompuGenericMath] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwDataDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_data
        if self.sw_data is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data, "CompuGenericMath")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependency":
        """Deserialize XML element to SwDataDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwDataDependency, cls).deserialize(element)

        # Parse sw_data
        child = SerializationHelper.find_child_element(element, "SW-DATA")
        if child is not None:
            sw_data_value = SerializationHelper.deserialize_by_tag(child, "CompuGenericMath")
            obj.sw_data = sw_data_value

        return obj



class SwDataDependencyBuilder:
    """Builder for SwDataDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependency = SwDataDependency()

    def build(self) -> SwDataDependency:
        """Build and return SwDataDependency object.

        Returns:
            SwDataDependency instance
        """
        # TODO: Add validation
        return self._obj
