"""HeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 152)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_HeapUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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


class HeapUsage(Identifiable, ABC):
    """AUTOSAR HeapUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    hardware: Optional[HardwareConfiguration]
    hw_element_ref: Optional[ARRef]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize HeapUsage."""
        super().__init__()
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self.software_context: Optional[SoftwareContext] = None

    def serialize(self) -> ET.Element:
        """Serialize HeapUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HeapUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hardware
        if self.hardware is not None:
            serialized = ARObject._serialize_item(self.hardware, "HardwareConfiguration")
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
            serialized = ARObject._serialize_item(self.hw_element_ref, "HwElement")
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
            serialized = ARObject._serialize_item(self.software_context, "SoftwareContext")
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
    def deserialize(cls, element: ET.Element) -> "HeapUsage":
        """Deserialize XML element to HeapUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HeapUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HeapUsage, cls).deserialize(element)

        # Parse hardware
        child = ARObject._find_child_element(element, "HARDWARE")
        if child is not None:
            hardware_value = ARObject._deserialize_by_tag(child, "HardwareConfiguration")
            obj.hardware = hardware_value

        # Parse hw_element_ref
        child = ARObject._find_child_element(element, "HW-ELEMENT-REF")
        if child is not None:
            hw_element_ref_value = ARRef.deserialize(child)
            obj.hw_element_ref = hw_element_ref_value

        # Parse software_context
        child = ARObject._find_child_element(element, "SOFTWARE-CONTEXT")
        if child is not None:
            software_context_value = ARObject._deserialize_by_tag(child, "SoftwareContext")
            obj.software_context = software_context_value

        return obj



class HeapUsageBuilder:
    """Builder for HeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HeapUsage = HeapUsage()

    def build(self) -> HeapUsage:
        """Build and return HeapUsage object.

        Returns:
            HeapUsage instance
        """
        # TODO: Add validation
        return self._obj
