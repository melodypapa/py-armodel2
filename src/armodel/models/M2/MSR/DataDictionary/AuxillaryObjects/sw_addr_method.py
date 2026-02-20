"""SwAddrMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 144)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 413)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_AuxillaryObjects.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import (
    MemoryAllocationKeywordPolicyType,
    MemorySectionType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    SectionInitializationPolicyType,
)


class SwAddrMethod(ARElement):
    """AUTOSAR SwAddrMethod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory: Optional[MemoryAllocationKeywordPolicyType]
    options: list[Identifier]
    section: Optional[SectionInitializationPolicyType]
    section_type: Optional[MemorySectionType]
    def __init__(self) -> None:
        """Initialize SwAddrMethod."""
        super().__init__()
        self.memory: Optional[MemoryAllocationKeywordPolicyType] = None
        self.options: list[Identifier] = []
        self.section: Optional[SectionInitializationPolicyType] = None
        self.section_type: Optional[MemorySectionType] = None

    def serialize(self) -> ET.Element:
        """Serialize SwAddrMethod to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAddrMethod, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize memory
        if self.memory is not None:
            serialized = ARObject._serialize_item(self.memory, "MemoryAllocationKeywordPolicyType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize options (list to container "OPTIONS")
        if self.options:
            wrapper = ET.Element("OPTIONS")
            for item in self.options:
                serialized = ARObject._serialize_item(item, "Identifier")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize section
        if self.section is not None:
            serialized = ARObject._serialize_item(self.section, "SectionInitializationPolicyType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize section_type
        if self.section_type is not None:
            serialized = ARObject._serialize_item(self.section_type, "MemorySectionType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECTION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAddrMethod":
        """Deserialize XML element to SwAddrMethod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAddrMethod object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAddrMethod, cls).deserialize(element)

        # Parse memory
        child = ARObject._find_child_element(element, "MEMORY")
        if child is not None:
            memory_value = MemoryAllocationKeywordPolicyType.deserialize(child)
            obj.memory = memory_value

        # Parse options (list from container "OPTIONS")
        obj.options = []
        container = ARObject._find_child_element(element, "OPTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.options.append(child_value)

        # Parse section
        child = ARObject._find_child_element(element, "SECTION")
        if child is not None:
            section_value = child.text
            obj.section = section_value

        # Parse section_type
        child = ARObject._find_child_element(element, "SECTION-TYPE")
        if child is not None:
            section_type_value = MemorySectionType.deserialize(child)
            obj.section_type = section_type_value

        return obj



class SwAddrMethodBuilder:
    """Builder for SwAddrMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAddrMethod = SwAddrMethod()

    def build(self) -> SwAddrMethod:
        """Build and return SwAddrMethod object.

        Returns:
            SwAddrMethod instance
        """
        # TODO: Add validation
        return self._obj
