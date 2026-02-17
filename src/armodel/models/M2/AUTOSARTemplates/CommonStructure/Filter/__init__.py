"""Filter module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
        DataFilter,
    )

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter_type_enum import (
    DataFilterTypeEnum,
)

__all__ = [
    "DataFilter",
    "DataFilterTypeEnum",
]
