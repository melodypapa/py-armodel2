"""MemorySectionLocation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
    MemorySection,
)


class MemorySectionLocation(ARObject):
    """AUTOSAR MemorySectionLocation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided_memory: Optional[HwElement]
    software: Optional[MemorySection]
    def __init__(self) -> None:
        """Initialize MemorySectionLocation."""
        super().__init__()
        self.provided_memory: Optional[HwElement] = None
        self.software: Optional[MemorySection] = None
    def serialize(self) -> ET.Element:
        """Serialize MemorySectionLocation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize provided_memory
        if self.provided_memory is not None:
            serialized = ARObject._serialize_item(self.provided_memory, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-MEMORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software
        if self.software is not None:
            serialized = ARObject._serialize_item(self.software, "MemorySection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySectionLocation":
        """Deserialize XML element to MemorySectionLocation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySectionLocation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse provided_memory
        child = ARObject._find_child_element(element, "PROVIDED-MEMORY")
        if child is not None:
            provided_memory_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.provided_memory = provided_memory_value

        # Parse software
        child = ARObject._find_child_element(element, "SOFTWARE")
        if child is not None:
            software_value = ARObject._deserialize_by_tag(child, "MemorySection")
            obj.software = software_value

        return obj



class MemorySectionLocationBuilder:
    """Builder for MemorySectionLocation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MemorySectionLocation = MemorySectionLocation()

    def build(self) -> MemorySectionLocation:
        """Build and return MemorySectionLocation object.

        Returns:
            MemorySectionLocation instance
        """
        # TODO: Add validation
        return self._obj
