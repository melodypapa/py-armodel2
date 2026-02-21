"""StackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2059)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)
from abc import ABC, abstractmethod


class StackUsage(Identifiable, ABC):
    """AUTOSAR StackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    executable_entity_ref: Optional[ARRef]
    hardware: Optional[HardwareConfiguration]
    hw_element_ref: Optional[ARRef]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize StackUsage."""
        super().__init__()
        self.executable_entity_ref: Optional[ARRef] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self.software_context: Optional[SoftwareContext] = None

    def serialize(self) -> ET.Element:
        """Serialize StackUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StackUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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
    def deserialize(cls, element: ET.Element) -> "StackUsage":
        """Deserialize XML element to StackUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StackUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StackUsage, cls).deserialize(element)

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

        # Parse software_context
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CONTEXT")
        if child is not None:
            software_context_value = SerializationHelper.deserialize_by_tag(child, "SoftwareContext")
            obj.software_context = software_context_value

        return obj



class StackUsageBuilder:
    """Builder for StackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StackUsage = StackUsage()

    def build(self) -> StackUsage:
        """Build and return StackUsage object.

        Returns:
            StackUsage instance
        """
        # TODO: Add validation
        return self._obj
