"""TcpOptionFilterSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)


class TcpOptionFilterSet(ARElement):
    """AUTOSAR TcpOptionFilterSet."""

    def __init__(self) -> None:
        """Initialize TcpOptionFilterSet."""
        super().__init__()
        self.tcp_option_filter_lists: list[TcpOptionFilterList] = []


class TcpOptionFilterSetBuilder:
    """Builder for TcpOptionFilterSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterSet = TcpOptionFilterSet()

    def build(self) -> TcpOptionFilterSet:
        """Build and return TcpOptionFilterSet object.

        Returns:
            TcpOptionFilterSet instance
        """
        # TODO: Add validation
        return self._obj
