"""MemorySectionLocation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    provided_memory_ref: Optional[ARRef]
    software_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize MemorySectionLocation."""
        super().__init__()
        self.provided_memory_ref: Optional[ARRef] = None
        self.software_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize MemorySectionLocation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MemorySectionLocation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_memory_ref
        if self.provided_memory_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_memory_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-MEMORY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software_ref
        if self.software_ref is not None:
            serialized = SerializationHelper.serialize_item(self.software_ref, "MemorySection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MemorySectionLocation, cls).deserialize(element)

        # Parse provided_memory_ref
        child = SerializationHelper.find_child_element(element, "PROVIDED-MEMORY-REF")
        if child is not None:
            provided_memory_ref_value = ARRef.deserialize(child)
            obj.provided_memory_ref = provided_memory_ref_value

        # Parse software_ref
        child = SerializationHelper.find_child_element(element, "SOFTWARE-REF")
        if child is not None:
            software_ref_value = ARRef.deserialize(child)
            obj.software_ref = software_ref_value

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
