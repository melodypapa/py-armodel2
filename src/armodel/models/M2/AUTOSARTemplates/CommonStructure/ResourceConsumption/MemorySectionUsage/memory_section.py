"""MemorySection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.section_name_prefix import (
    SectionNamePrefix,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)


class MemorySection(Identifiable):
    """AUTOSAR MemorySection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alignment", None, True, False, None),  # alignment
        ("executable_entities", None, False, True, ExecutableEntity),  # executableEntities
        ("options", None, False, True, None),  # options
        ("prefix", None, False, False, SectionNamePrefix),  # prefix
        ("size", None, True, False, None),  # size
        ("sw_addrmethod", None, False, False, SwAddrMethod),  # swAddrmethod
        ("symbol", None, True, False, None),  # symbol
    ]

    def __init__(self) -> None:
        """Initialize MemorySection."""
        super().__init__()
        self.alignment: Optional[AlignmentType] = None
        self.executable_entities: list[ExecutableEntity] = []
        self.options: list[Identifier] = []
        self.prefix: Optional[SectionNamePrefix] = None
        self.size: Optional[PositiveInteger] = None
        self.sw_addrmethod: Optional[SwAddrMethod] = None
        self.symbol: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MemorySection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySection":
        """Create MemorySection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MemorySection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MemorySection since parent returns ARObject
        return cast("MemorySection", obj)


class MemorySectionBuilder:
    """Builder for MemorySection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MemorySection = MemorySection()

    def build(self) -> MemorySection:
        """Build and return MemorySection object.

        Returns:
            MemorySection instance
        """
        # TODO: Add validation
        return self._obj
