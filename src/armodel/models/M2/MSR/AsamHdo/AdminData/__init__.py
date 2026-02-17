"""AdminData module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
        AdminData,
    )
    from armodel.models.M2.MSR.AsamHdo.AdminData.doc_revision import (
        DocRevision,
    )
    from armodel.models.M2.MSR.AsamHdo.AdminData.modification import (
        Modification,
    )

__all__ = [
    "AdminData",
    "DocRevision",
    "Modification",
]
