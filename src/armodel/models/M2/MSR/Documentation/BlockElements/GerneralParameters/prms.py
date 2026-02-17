"""Prms AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_GerneralParameters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class Prms(Paginateable):
    """AUTOSAR Prms."""

    label: Optional[MultilanguageLongName]
    prm: Any
    def __init__(self) -> None:
        """Initialize Prms."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.prm: Any = None


class PrmsBuilder:
    """Builder for Prms."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Prms = Prms()

    def build(self) -> Prms:
        """Build and return Prms object.

        Returns:
            Prms instance
        """
        # TODO: Add validation
        return self._obj
