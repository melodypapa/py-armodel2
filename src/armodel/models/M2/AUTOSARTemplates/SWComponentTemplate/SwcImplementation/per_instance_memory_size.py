"""PerInstanceMemorySize AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class PerInstanceMemorySize(ARObject):
    """AUTOSAR PerInstanceMemorySize."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[PositiveInteger]
    per_instance_memory_memory_ref: Optional[ARRef]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory_ref: Optional[ARRef] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize PerInstanceMemorySize to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PerInstanceMemorySize, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "PositiveInteger")
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

        # Serialize per_instance_memory_memory_ref
        if self.per_instance_memory_memory_ref is not None:
            serialized = SerializationHelper.serialize_item(self.per_instance_memory_memory_ref, "PerInstanceMemory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PER-INSTANCE-MEMORY-MEMORY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = SerializationHelper.serialize_item(self.size, "PositiveInteger")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemorySize":
        """Deserialize XML element to PerInstanceMemorySize object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PerInstanceMemorySize object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PerInstanceMemorySize, cls).deserialize(element)

        # Parse alignment
        child = SerializationHelper.find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse per_instance_memory_memory_ref
        child = SerializationHelper.find_child_element(element, "PER-INSTANCE-MEMORY-MEMORY-REF")
        if child is not None:
            per_instance_memory_memory_ref_value = ARRef.deserialize(child)
            obj.per_instance_memory_memory_ref = per_instance_memory_memory_ref_value

        # Parse size
        child = SerializationHelper.find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        return obj



class PerInstanceMemorySizeBuilder:
    """Builder for PerInstanceMemorySize."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemorySize = PerInstanceMemorySize()

    def build(self) -> PerInstanceMemorySize:
        """Build and return PerInstanceMemorySize object.

        Returns:
            PerInstanceMemorySize instance
        """
        # TODO: Add validation
        return self._obj
