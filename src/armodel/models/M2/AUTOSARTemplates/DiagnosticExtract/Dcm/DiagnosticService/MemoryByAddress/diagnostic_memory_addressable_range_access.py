"""DiagnosticMemoryAddressableRangeAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """AUTOSAR DiagnosticMemoryAddressableRangeAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    memory_range_refs: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryAddressableRangeAccess."""
        super().__init__()
        self.memory_range_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryAddressableRangeAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryAddressableRangeAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize memory_range_refs (list to container "MEMORY-RANGE-REFS")
        if self.memory_range_refs:
            wrapper = ET.Element("MEMORY-RANGE-REFS")
            for item in self.memory_range_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("MEMORY-RANGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryAddressableRangeAccess":
        """Deserialize XML element to DiagnosticMemoryAddressableRangeAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryAddressableRangeAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryAddressableRangeAccess, cls).deserialize(element)

        # Parse memory_range_refs (list from container "MEMORY-RANGE-REFS")
        obj.memory_range_refs = []
        container = SerializationHelper.find_child_element(element, "MEMORY-RANGE-REFS")
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
                    obj.memory_range_refs.append(child_value)

        return obj



class DiagnosticMemoryAddressableRangeAccessBuilder:
    """Builder for DiagnosticMemoryAddressableRangeAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryAddressableRangeAccess = DiagnosticMemoryAddressableRangeAccess()

    def build(self) -> DiagnosticMemoryAddressableRangeAccess:
        """Build and return DiagnosticMemoryAddressableRangeAccess object.

        Returns:
            DiagnosticMemoryAddressableRangeAccess instance
        """
        # TODO: Add validation
        return self._obj
