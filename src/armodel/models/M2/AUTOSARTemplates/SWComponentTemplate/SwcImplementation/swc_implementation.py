"""SwcImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 344)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2069)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcImplementation(Implementation):
    """AUTOSAR SwcImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior: Optional[SwcInternalBehavior]
    per_instance_memories: list[PerInstanceMemory]
    required: Optional[String]
    def __init__(self) -> None:
        """Initialize SwcImplementation."""
        super().__init__()
        self.behavior: Optional[SwcInternalBehavior] = None
        self.per_instance_memories: list[PerInstanceMemory] = []
        self.required: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior
        if self.behavior is not None:
            serialized = ARObject._serialize_item(self.behavior, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize per_instance_memories (list to container "PER-INSTANCE-MEMORIES")
        if self.per_instance_memories:
            wrapper = ET.Element("PER-INSTANCE-MEMORIES")
            for item in self.per_instance_memories:
                serialized = ARObject._serialize_item(item, "PerInstanceMemory")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required
        if self.required is not None:
            serialized = ARObject._serialize_item(self.required, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcImplementation":
        """Deserialize XML element to SwcImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcImplementation, cls).deserialize(element)

        # Parse behavior
        child = ARObject._find_child_element(element, "BEHAVIOR")
        if child is not None:
            behavior_value = ARObject._deserialize_by_tag(child, "SwcInternalBehavior")
            obj.behavior = behavior_value

        # Parse per_instance_memories (list from container "PER-INSTANCE-MEMORIES")
        obj.per_instance_memories = []
        container = ARObject._find_child_element(element, "PER-INSTANCE-MEMORIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memories.append(child_value)

        # Parse required
        child = ARObject._find_child_element(element, "REQUIRED")
        if child is not None:
            required_value = child.text
            obj.required = required_value

        return obj



class SwcImplementationBuilder:
    """Builder for SwcImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcImplementation = SwcImplementation()

    def build(self) -> SwcImplementation:
        """Build and return SwcImplementation object.

        Returns:
            SwcImplementation instance
        """
        # TODO: Add validation
        return self._obj
