"""DocumentationOnM1 module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
        Documentation,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation_context import (
        DocumentationContext,
    )

from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.standard_name_enum import (
    StandardNameEnum,
)

__all__ = [
    "Documentation",
    "DocumentationContext",
    "StandardNameEnum",
]
