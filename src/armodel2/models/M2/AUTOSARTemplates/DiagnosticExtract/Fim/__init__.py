"""Fim module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_alias_event import (
        DiagnosticFimAliasEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_function_identifier import (
        DiagnosticFunctionIdentifier,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_function_identifier_inhibit import (
        DiagnosticFunctionIdentifierInhibit,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_function_inhibit_source import (
        DiagnosticFunctionInhibitSource,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
        DiagnosticFimEventGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_alias_event_group import (
        DiagnosticFimAliasEventGroup,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_inhibition_mask_enum import (
    DiagnosticInhibitionMaskEnum,
)

__all__ = [
    "DiagnosticFimAliasEvent",
    "DiagnosticFimAliasEventGroup",
    "DiagnosticFimEventGroup",
    "DiagnosticFunctionIdentifier",
    "DiagnosticFunctionIdentifierInhibit",
    "DiagnosticFunctionInhibitSource",
    "DiagnosticInhibitionMaskEnum",
]
