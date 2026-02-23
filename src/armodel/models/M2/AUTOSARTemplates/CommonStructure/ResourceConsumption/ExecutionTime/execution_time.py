"""ExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 159)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2025)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.memory_section_location import (
    MemorySectionLocation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)
from abc import ABC, abstractmethod


class ExecutionTime(Identifiable, ABC):
    """AUTOSAR ExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    exclusive_area_ref: Optional[ARRef]
    executable_entity_ref: Optional[ARRef]
    hardware: Optional[HardwareConfiguration]
    hw_element_ref: Optional[ARRef]
    _included_librarie_refs: list[ARRef]
    memory_section_locations: list[MemorySectionLocation]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize ExecutionTime."""
        super().__init__()
        self.exclusive_area_ref: Optional[ARRef] = None
        self.executable_entity_ref: Optional[ARRef] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self._included_librarie_refs: list[ARRef] = []
        self.memory_section_locations: list[MemorySectionLocation] = []
        self.software_context: Optional[SoftwareContext] = None
    @property
    @xml_element_name("INCLUDED-LIBRARYS")
    def included_librarie_refs(self) -> list[ARRef]:
        """Get included_librarie_refs with custom XML element name."""
        return self._included_librarie_refs

    @included_librarie_refs.setter
    def included_librarie_refs(self, value: list[ARRef]) -> None:
        """Set included_librarie_refs with custom XML element name."""
        self._included_librarie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize ExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize exclusive_area_ref
        if self.exclusive_area_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exclusive_area_ref, "ExclusiveArea")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCLUSIVE-AREA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entity_ref
        if self.executable_entity_ref is not None:
            serialized = SerializationHelper.serialize_item(self.executable_entity_ref, "ExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTABLE-ENTITY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hardware
        if self.hardware is not None:
            serialized = SerializationHelper.serialize_item(self.hardware, "HardwareConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HARDWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_element_ref
        if self.hw_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_element_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize included_librarie_refs (list to container "INCLUDED-LIBRARYS")
        if self.included_librarie_refs:
            wrapper = ET.Element("INCLUDED-LIBRARYS")
            for item in self.included_librarie_refs:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-LIBRARIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize memory_section_locations (list to container "MEMORY-SECTION-LOCATIONS")
        if self.memory_section_locations:
            wrapper = ET.Element("MEMORY-SECTION-LOCATIONS")
            for item in self.memory_section_locations:
                serialized = SerializationHelper.serialize_item(item, "MemorySectionLocation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_context
        if self.software_context is not None:
            serialized = SerializationHelper.serialize_item(self.software_context, "SoftwareContext")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTime":
        """Deserialize XML element to ExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutionTime, cls).deserialize(element)

        # Parse exclusive_area_ref
        child = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-REF")
        if child is not None:
            exclusive_area_ref_value = ARRef.deserialize(child)
            obj.exclusive_area_ref = exclusive_area_ref_value

        # Parse executable_entity_ref
        child = SerializationHelper.find_child_element(element, "EXECUTABLE-ENTITY-REF")
        if child is not None:
            executable_entity_ref_value = ARRef.deserialize(child)
            obj.executable_entity_ref = executable_entity_ref_value

        # Parse hardware
        child = SerializationHelper.find_child_element(element, "HARDWARE")
        if child is not None:
            hardware_value = SerializationHelper.deserialize_by_tag(child, "HardwareConfiguration")
            obj.hardware = hardware_value

        # Parse hw_element_ref
        child = SerializationHelper.find_child_element(element, "HW-ELEMENT-REF")
        if child is not None:
            hw_element_ref_value = ARRef.deserialize(child)
            obj.hw_element_ref = hw_element_ref_value

        # Parse included_librarie_refs (list from container "INCLUDED-LIBRARYS")
        obj.included_librarie_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-LIBRARYS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_librarie_refs.append(child_value)

        # Parse memory_section_locations (list from container "MEMORY-SECTION-LOCATIONS")
        obj.memory_section_locations = []
        container = SerializationHelper.find_child_element(element, "MEMORY-SECTION-LOCATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.memory_section_locations.append(child_value)

        # Parse software_context
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CONTEXT")
        if child is not None:
            software_context_value = SerializationHelper.deserialize_by_tag(child, "SoftwareContext")
            obj.software_context = software_context_value

        return obj



