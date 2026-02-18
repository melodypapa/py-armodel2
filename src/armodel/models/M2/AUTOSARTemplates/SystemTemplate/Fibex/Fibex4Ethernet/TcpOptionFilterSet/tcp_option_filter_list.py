"""TcpOptionFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_tcp_options: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []


class TcpOptionFilterListBuilder:
    """Builder for TcpOptionFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterList = TcpOptionFilterList()

    def build(self) -> TcpOptionFilterList:
        """Build and return TcpOptionFilterList object.

        Returns:
            TcpOptionFilterList instance
        """
        # TODO: Add validation
        return self._obj
