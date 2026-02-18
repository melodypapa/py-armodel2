"""BuildActionEntity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_invocator import (
    BuildActionInvocator,
)
from abc import ABC, abstractmethod


class BuildActionEntity(Identifiable, ABC):
    """AUTOSAR BuildActionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    delivery_artifacts: list[AutosarEngineeringObject]
    invocation: Optional[BuildActionInvocator]
    def __init__(self) -> None:
        """Initialize BuildActionEntity."""
        super().__init__()
        self.delivery_artifacts: list[AutosarEngineeringObject] = []
        self.invocation: Optional[BuildActionInvocator] = None


class BuildActionEntityBuilder:
    """Builder for BuildActionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEntity = BuildActionEntity()

    def build(self) -> BuildActionEntity:
        """Build and return BuildActionEntity object.

        Returns:
            BuildActionEntity instance
        """
        # TODO: Add validation
        return self._obj
