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
