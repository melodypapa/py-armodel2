"""IntrusionDetectionSystem module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.ids_platform_instantiation import (
        IdsPlatformInstantiation,
    )
    from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.idsm_module_instantiation import (
        IdsmModuleInstantiation,
    )

__all__ = [
    "IdsPlatformInstantiation",
    "IdsmModuleInstantiation",
]
