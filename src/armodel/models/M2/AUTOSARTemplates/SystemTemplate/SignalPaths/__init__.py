"""SignalPaths module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.common_signal_path import (
    CommonSignalPath,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_operation_arguments import (
    SwcToSwcOperationArguments,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.forbidden_signal_path import (
    ForbiddenSignalPath,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.permissible_signal_path import (
    PermissibleSignalPath,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.separate_signal_path import (
    SeparateSignalPath,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)

__all__ = [
    "CommonSignalPath",
    "ForbiddenSignalPath",
    "PermissibleSignalPath",
    "SeparateSignalPath",
    "SignalPathConstraint",
    "SwcToSwcOperationArguments",
    "SwcToSwcSignal",
]
