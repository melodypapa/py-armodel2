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
