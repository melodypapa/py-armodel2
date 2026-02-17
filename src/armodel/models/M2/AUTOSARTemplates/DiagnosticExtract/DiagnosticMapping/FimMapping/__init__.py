"""FimMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.FimMapping.diagnostic_inhibit_source_event_mapping import (
        DiagnosticInhibitSourceEventMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.FimMapping.diagnostic_fim_alias_event_group_mapping import (
        DiagnosticFimAliasEventGroupMapping,
    )

__all__ = [
    "DiagnosticFimAliasEventGroupMapping",
    "DiagnosticInhibitSourceEventMapping",
]
