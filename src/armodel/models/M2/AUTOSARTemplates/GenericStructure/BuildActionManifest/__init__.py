"""BuildActionManifest module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_manifest import (
        BuildActionManifest,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
        BuildAction,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_io_element import (
        BuildActionIoElement,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
        BuildActionEnvironment,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import (
        BuildActionEntity,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_invocator import (
        BuildActionInvocator,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_engineering_object import (
        BuildEngineeringObject,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.generic_model_reference import (
        GenericModelReference,
    )

__all__ = [
    "BuildAction",
    "BuildActionEntity",
    "BuildActionEnvironment",
    "BuildActionInvocator",
    "BuildActionIoElement",
    "BuildActionManifest",
    "BuildEngineeringObject",
    "GenericModelReference",
]
