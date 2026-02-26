"""AbstractPlatform module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.AbstractPlatform.application_interface import (
        ApplicationInterface,
    )
    from armodel2.models.M2.AUTOSARTemplates.AbstractPlatform.application_deferred_data_type import (
        ApplicationDeferredDataType,
    )

__all__ = [
    "ApplicationDeferredDataType",
    "ApplicationInterface",
]
