"""FreeFormat AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.free_format_entry import (
    FreeFormatEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FreeFormat(FreeFormatEntry):
    """AUTOSAR FreeFormat."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    byte_values: list[Integer]
    def __init__(self) -> None:
        """Initialize FreeFormat."""
        super().__init__()
        self.byte_values: list[Integer] = []
    def serialize(self) -> ET.Element:
        """Serialize FreeFormat to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FreeFormat, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize byte_values (list to container "BYTE-VALUES")
        if self.byte_values:
            wrapper = ET.Element("BYTE-VALUES")
            for item in self.byte_values:
                serialized = ARObject._serialize_item(item, "Integer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FreeFormat":
        """Deserialize XML element to FreeFormat object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FreeFormat object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FreeFormat, cls).deserialize(element)

        # Parse byte_values (list from container "BYTE-VALUES")
        obj.byte_values = []
        container = ARObject._find_child_element(element, "BYTE-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.byte_values.append(child_value)

        return obj



class FreeFormatBuilder:
    """Builder for FreeFormat."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FreeFormat = FreeFormat()

    def build(self) -> FreeFormat:
        """Build and return FreeFormat object.

        Returns:
            FreeFormat instance
        """
        # TODO: Add validation
        return self._obj
