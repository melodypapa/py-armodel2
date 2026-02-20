"""SwDataDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 373)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sw_data
        if self.sw_data is not None:
            serialized = ARObject._serialize_item(self.sw_data, "CompuGenericMath")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_data
        child = ARObject._find_child_element(element, "SW-DATA")
        if child is not None:
            sw_data_value = ARObject._deserialize_by_tag(child, "CompuGenericMath")
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
