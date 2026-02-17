"""IdsmModuleInstantiation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_IntrusionDetectionSystem.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.ids_platform_instantiation import (
    IdsPlatformInstantiation,
)


class IdsmModuleInstantiation(IdsPlatformInstantiation):
    """AUTOSAR IdsmModuleInstantiation."""

    def __init__(self) -> None:
        """Initialize IdsmModuleInstantiation."""
        super().__init__()


class IdsmModuleInstantiationBuilder:
    """Builder for IdsmModuleInstantiation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmModuleInstantiation = IdsmModuleInstantiation()

    def build(self) -> IdsmModuleInstantiation:
        """Build and return IdsmModuleInstantiation object.

        Returns:
            IdsmModuleInstantiation instance
        """
        # TODO: Add validation
        return self._obj
