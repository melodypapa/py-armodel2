"""SignalPaths module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.common_signal_path import (
        CommonSignalPath,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
        SwcToSwcSignal,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_operation_arguments import (
        SwcToSwcOperationArguments,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.forbidden_signal_path import (
        ForbiddenSignalPath,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.permissible_signal_path import (
        PermissibleSignalPath,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.separate_signal_path import (
        SeparateSignalPath,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
        SignalPathConstraint,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_operation_arguments_direction_enum import (
    SwcToSwcOperationArgumentsDirectionEnum,
)

__all__ = [
    "CommonSignalPath",
    "ForbiddenSignalPath",
    "PermissibleSignalPath",
    "SeparateSignalPath",
    "SignalPathConstraint",
    "SwcToSwcOperationArguments",
    "SwcToSwcOperationArgumentsDirectionEnum",
    "SwcToSwcSignal",
]
