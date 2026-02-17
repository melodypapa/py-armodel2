"""DatadictionaryProxies module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
        SwCalprmRefProxy,
    )
    from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
        SwVariableRefProxy,
    )

__all__ = [
    "SwCalprmRefProxy",
    "SwVariableRefProxy",
]
