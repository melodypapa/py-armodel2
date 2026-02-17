"""Paginateable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 339)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import (
    DocumentViewSelectable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    KeepWithPreviousEnum,
)


class Paginateable(DocumentViewSelectable):
    """AUTOSAR Paginateable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "break_": XMLMember(
            xml_tag='BREAK',
            is_attribute=False,
            multiplicity="0..1",
            element_class=ChapterEnumBreak,
            xml_name_override='BREAK',
        ),  # break
        "keep_with": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=KeepWithPreviousEnum,
        ),  # keepWith
    }

    def __init__(self) -> None:
        """Initialize Paginateable."""
        super().__init__()
        self.break_: Optional[ChapterEnumBreak] = None
        self.keep_with: Optional[KeepWithPreviousEnum] = None


class PaginateableBuilder:
    """Builder for Paginateable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Paginateable = Paginateable()

    def build(self) -> Paginateable:
        """Build and return Paginateable object.

        Returns:
            Paginateable instance
        """
        # TODO: Add validation
        return self._obj
