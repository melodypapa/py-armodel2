"""RecordLayout module."""

from __future__ import annotations
from typing import TYPE_CHECKING

from armodel2.models.M2.MSR.DataDictionary.RecordLayout.axis_index_type import (
    AxisIndexType,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.record_layout_iterator_point import (
    RecordLayoutIteratorPoint,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.asam_record_layout_semantics import (
    AsamRecordLayoutSemantics,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
        SwRecordLayout,
    )
    from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
        SwRecordLayoutV,
    )
    from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
        SwRecordLayoutGroup,
    )
    from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group_content import (
        SwRecordLayoutGroupContent,
    )

__all__ = [
    "AsamRecordLayoutSemantics",
    "AxisIndexType",
    "RecordLayoutIteratorPoint",
    "SwRecordLayout",
    "SwRecordLayoutGroup",
    "SwRecordLayoutGroupContent",
    "SwRecordLayoutV",
]
