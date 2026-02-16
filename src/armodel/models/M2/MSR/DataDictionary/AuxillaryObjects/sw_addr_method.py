"""SwAddrMethod AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    SectionInitializationPolicyType,
)


class SwAddrMethod(ARElement):
    """AUTOSAR SwAddrMethod."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("memory", None, False, False, MemoryAllocationKeywordPolicyType),  # memory
        ("options", None, False, True, None),  # options
        ("section", None, True, False, None),  # section
        ("section_type", None, False, False, MemorySectionType),  # sectionType
    ]

    def __init__(self) -> None:
        """Initialize SwAddrMethod."""
        super().__init__()
        self.memory: Optional[MemoryAllocationKeywordPolicyType] = None
        self.options: list[Identifier] = []
        self.section: Optional[SectionInitializationPolicyType] = None
        self.section_type: Optional[MemorySectionType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwAddrMethod to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAddrMethod":
        """Create SwAddrMethod from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwAddrMethod instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwAddrMethod since parent returns ARObject
        return cast("SwAddrMethod", obj)


class SwAddrMethodBuilder:
    """Builder for SwAddrMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAddrMethod = SwAddrMethod()

    def build(self) -> SwAddrMethod:
        """Build and return SwAddrMethod object.

        Returns:
            SwAddrMethod instance
        """
        # TODO: Add validation
        return self._obj
