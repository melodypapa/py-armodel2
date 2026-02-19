"""MemorySection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 143)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 411)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2036)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[AlignmentType]
    executable_entities: list[ExecutableEntity]
    options: list[Identifier]
    prefix: Optional[SectionNamePrefix]
    size: Optional[PositiveInteger]
    sw_addrmethod: Optional[SwAddrMethod]
    symbol: Optional[Identifier]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySection":
        """Deserialize XML element to MemorySection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse executable_entities (list)
        obj.executable_entities = []
        for child in ARObject._find_all_child_elements(element, "EXECUTABLE-ENTITIES"):
            executable_entities_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.executable_entities.append(executable_entities_value)

        # Parse options (list)
        obj.options = []
        for child in ARObject._find_all_child_elements(element, "OPTIONS"):
            options_value = child.text
            obj.options.append(options_value)

        # Parse prefix
        child = ARObject._find_child_element(element, "PREFIX")
        if child is not None:
            prefix_value = ARObject._deserialize_by_tag(child, "SectionNamePrefix")
            obj.prefix = prefix_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        # Parse sw_addrmethod
        child = ARObject._find_child_element(element, "SW-ADDRMETHOD")
        if child is not None:
            sw_addrmethod_value = ARObject._deserialize_by_tag(child, "SwAddrMethod")
            obj.sw_addrmethod = sw_addrmethod_value

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
            obj.symbol = symbol_value

        return obj



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
