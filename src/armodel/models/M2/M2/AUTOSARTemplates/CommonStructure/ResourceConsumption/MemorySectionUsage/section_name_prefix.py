"""SectionNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 147)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in: Optional[DependencyOnArtifact] = None


class SectionNamePrefixBuilder:
    """Builder for SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SectionNamePrefix = SectionNamePrefix()

    def build(self) -> SectionNamePrefix:
        """Build and return SectionNamePrefix object.

        Returns:
            SectionNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
