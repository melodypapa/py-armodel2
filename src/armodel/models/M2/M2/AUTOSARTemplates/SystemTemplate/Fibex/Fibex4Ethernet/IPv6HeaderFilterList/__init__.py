"""IPv6HeaderFilterList module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_set import (
        IPv6ExtHeaderFilterSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
        IPv6ExtHeaderFilterList,
    )

__all__ = [
    "IPv6ExtHeaderFilterList",
    "IPv6ExtHeaderFilterSet",
]
