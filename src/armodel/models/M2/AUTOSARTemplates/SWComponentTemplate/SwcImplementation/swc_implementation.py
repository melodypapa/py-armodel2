"""SwcImplementation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("behavior", None, False, False, SwcInternalBehavior),  # behavior
        ("per_instance_memories", None, False, True, PerInstanceMemory),  # perInstanceMemories
        ("required", None, True, False, None),  # required
    ]

    def __init__(self) -> None:
        """Initialize SwcImplementation."""
        super().__init__()
        self.behavior: Optional[SwcInternalBehavior] = None
        self.per_instance_memories: list[PerInstanceMemory] = []
        self.required: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcImplementation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcImplementation":
        """Create SwcImplementation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcImplementation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcImplementation since parent returns ARObject
        return cast("SwcImplementation", obj)


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
