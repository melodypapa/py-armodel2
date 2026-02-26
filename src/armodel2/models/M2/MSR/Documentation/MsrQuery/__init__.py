"""MsrQuery module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
        MsrQueryP1,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
        MsrQueryTopic1,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_chapter import (
        MsrQueryChapter,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
        MsrQueryProps,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_arg import (
        MsrQueryArg,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
        MsrQueryResultChapter,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_result_topic1 import (
        MsrQueryResultTopic1,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p2 import (
        MsrQueryP2,
    )

__all__ = [
    "MsrQueryArg",
    "MsrQueryChapter",
    "MsrQueryP1",
    "MsrQueryP2",
    "MsrQueryProps",
    "MsrQueryResultChapter",
    "MsrQueryResultTopic1",
    "MsrQueryTopic1",
]
