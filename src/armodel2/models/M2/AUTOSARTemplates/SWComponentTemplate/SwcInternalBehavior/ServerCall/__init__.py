"""ServerCall module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.asynchronous_server_call_result_point import (
        AsynchronousServerCallResultPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
        ServerCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.synchronous_server_call_point import (
        SynchronousServerCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.asynchronous_server_call_point import (
        AsynchronousServerCallPoint,
    )

__all__ = [
    "AsynchronousServerCallPoint",
    "AsynchronousServerCallResultPoint",
    "ServerCallPoint",
    "SynchronousServerCallPoint",
]
