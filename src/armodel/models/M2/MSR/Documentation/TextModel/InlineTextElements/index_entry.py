"""IndexEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 317)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)


class IndexEntry(ARObject):
    """AUTOSAR IndexEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sub": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sub
        "sup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sup
    }

    def __init__(self) -> None:
        """Initialize IndexEntry."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None


class IndexEntryBuilder:
    """Builder for IndexEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexEntry = IndexEntry()

    def build(self) -> IndexEntry:
        """Build and return IndexEntry object.

        Returns:
            IndexEntry instance
        """
        # TODO: Add validation
        return self._obj
