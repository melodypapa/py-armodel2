"""PerInstanceMemorySize AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class PerInstanceMemorySize(ARObject):
    """AUTOSAR PerInstanceMemorySize."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alignment", None, True, False, None),  # alignment
        ("per_instance_memory_memory", None, False, False, PerInstanceMemory),  # perInstanceMemoryMemory
        ("size", None, True, False, None),  # size
    ]

    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory: Optional[PerInstanceMemory] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PerInstanceMemorySize to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemorySize":
        """Create PerInstanceMemorySize from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PerInstanceMemorySize instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PerInstanceMemorySize since parent returns ARObject
        return cast("PerInstanceMemorySize", obj)


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
