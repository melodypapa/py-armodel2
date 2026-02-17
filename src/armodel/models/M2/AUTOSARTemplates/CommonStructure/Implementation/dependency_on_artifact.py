"""DependencyOnArtifact AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 131)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    DependencyUsageEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)


class DependencyOnArtifact(Identifiable):
    """AUTOSAR DependencyOnArtifact."""

    def __init__(self) -> None:
        """Initialize DependencyOnArtifact."""
        super().__init__()
        self.artifact: Optional[AutosarEngineeringObject] = None
        self.usages: list[DependencyUsageEnum] = []


class DependencyOnArtifactBuilder:
    """Builder for DependencyOnArtifact."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DependencyOnArtifact = DependencyOnArtifact()

    def build(self) -> DependencyOnArtifact:
        """Build and return DependencyOnArtifact object.

        Returns:
            DependencyOnArtifact instance
        """
        # TODO: Add validation
        return self._obj
