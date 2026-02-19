"""MemorySection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 143)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 411)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2036)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.section_name_prefix import (
    SectionNamePrefix,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)


class MemorySection(Identifiable):
    """AUTOSAR MemorySection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[AlignmentType]
    executable_entities: list[ExecutableEntity]
    options: list[Identifier]
    prefix: Optional[SectionNamePrefix]
    size: Optional[PositiveInteger]
    sw_addrmethod: Optional[SwAddrMethod]
    symbol: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize MemorySection."""
        super().__init__()
        self.alignment: Optional[AlignmentType] = None
        self.executable_entities: list[ExecutableEntity] = []
        self.options: list[Identifier] = []
        self.prefix: Optional[SectionNamePrefix] = None
        self.size: Optional[PositiveInteger] = None
        self.sw_addrmethod: Optional[SwAddrMethod] = None
        self.symbol: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize MemorySection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MemorySection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = ARObject._serialize_item(self.alignment, "AlignmentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entities (list to container "EXECUTABLE-ENTITIES")
        if self.executable_entities:
            wrapper = ET.Element("EXECUTABLE-ENTITIES")
            for item in self.executable_entities:
                serialized = ARObject._serialize_item(item, "ExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize options (list to container "OPTIONS")
        if self.options:
            wrapper = ET.Element("OPTIONS")
            for item in self.options:
                serialized = ARObject._serialize_item(item, "Identifier")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prefix
        if self.prefix is not None:
            serialized = ARObject._serialize_item(self.prefix, "SectionNamePrefix")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = ARObject._serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_addrmethod
        if self.sw_addrmethod is not None:
            serialized = ARObject._serialize_item(self.sw_addrmethod, "SwAddrMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ADDRMETHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol
        if self.symbol is not None:
            serialized = ARObject._serialize_item(self.symbol, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySection":
        """Deserialize XML element to MemorySection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MemorySection, cls).deserialize(element)

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse executable_entities (list from container "EXECUTABLE-ENTITIES")
        obj.executable_entities = []
        container = ARObject._find_child_element(element, "EXECUTABLE-ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.executable_entities.append(child_value)

        # Parse options (list from container "OPTIONS")
        obj.options = []
        container = ARObject._find_child_element(element, "OPTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.options.append(child_value)

        # Parse prefix
        child = ARObject._find_child_element(element, "PREFIX")
        if child is not None:
            prefix_value = ARObject._deserialize_by_tag(child, "SectionNamePrefix")
            obj.prefix = prefix_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        # Parse sw_addrmethod
        child = ARObject._find_child_element(element, "SW-ADDRMETHOD")
        if child is not None:
            sw_addrmethod_value = ARObject._deserialize_by_tag(child, "SwAddrMethod")
            obj.sw_addrmethod = sw_addrmethod_value

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.symbol = symbol_value

        return obj



class MemorySectionBuilder:
    """Builder for MemorySection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MemorySection = MemorySection()

    def build(self) -> MemorySection:
        """Build and return MemorySection object.

        Returns:
            MemorySection instance
        """
        # TODO: Add validation
        return self._obj
