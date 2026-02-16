"""MemorySectionLocation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
    MemorySection,
)


class MemorySectionLocation(ARObject):
    """AUTOSAR MemorySectionLocation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provided_memory", None, False, False, HwElement),  # providedMemory
        ("software", None, False, False, MemorySection),  # software
    ]

    def __init__(self) -> None:
        """Initialize MemorySectionLocation."""
        super().__init__()
        self.provided_memory: Optional[HwElement] = None
        self.software: Optional[MemorySection] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MemorySectionLocation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySectionLocation":
        """Create MemorySectionLocation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MemorySectionLocation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MemorySectionLocation since parent returns ARObject
        return cast("MemorySectionLocation", obj)


class MemorySectionLocationBuilder:
    """Builder for MemorySectionLocation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MemorySectionLocation = MemorySectionLocation()

    def build(self) -> MemorySectionLocation:
        """Build and return MemorySectionLocation object.

        Returns:
            MemorySectionLocation instance
        """
        # TODO: Add validation
        return self._obj
