"""EndToEndProtection module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_description import (
        EndToEndDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection_set import (
        EndToEndProtectionSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection import (
        EndToEndProtection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection_variable_prototype import (
        EndToEndProtectionVariablePrototype,
    )

__all__ = [
    "EndToEndDescription",
    "EndToEndProtection",
    "EndToEndProtectionSet",
    "EndToEndProtectionVariablePrototype",
]
