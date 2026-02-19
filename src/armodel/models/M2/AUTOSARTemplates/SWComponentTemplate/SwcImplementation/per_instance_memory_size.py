"""PerInstanceMemorySize AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    per_instance_memory_memory: Optional[PerInstanceMemory]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory: Optional[PerInstanceMemory] = None
        self.size: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemorySize":
        """Deserialize XML element to PerInstanceMemorySize object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PerInstanceMemorySize object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse per_instance_memory_memory
        child = ARObject._find_child_element(element, "PER-INSTANCE-MEMORY-MEMORY")
        if child is not None:
            per_instance_memory_memory_value = ARObject._deserialize_by_tag(child, "PerInstanceMemory")
            obj.per_instance_memory_memory = per_instance_memory_memory_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
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
