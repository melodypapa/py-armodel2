"""MixedContentForVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from abc import ABC, abstractmethod


class MixedContentForVerbatim(ARObject, ABC):
    """AUTOSAR MixedContentForVerbatim."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    br: Br
    e: EmphasisText
    tt: Tt
    xref: Xref
    def __init__(self) -> None:
        """Initialize MixedContentForVerbatim."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.tt: Tt = None
        self.xref: Xref = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForVerbatim":
        """Deserialize XML element to MixedContentForVerbatim object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForVerbatim object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse br
        child = ARObject._find_child_element(element, "BR")
        if child is not None:
            br_value = ARObject._deserialize_by_tag(child, "Br")
            obj.br = br_value

        # Parse e
        child = ARObject._find_child_element(element, "E")
        if child is not None:
            e_value = ARObject._deserialize_by_tag(child, "EmphasisText")
            obj.e = e_value

        # Parse tt
        child = ARObject._find_child_element(element, "TT")
        if child is not None:
            tt_value = ARObject._deserialize_by_tag(child, "Tt")
            obj.tt = tt_value

        # Parse xref
        child = ARObject._find_child_element(element, "XREF")
        if child is not None:
            xref_value = ARObject._deserialize_by_tag(child, "Xref")
            obj.xref = xref_value

        return obj



class MixedContentForVerbatimBuilder:
    """Builder for MixedContentForVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForVerbatim = MixedContentForVerbatim()

    def build(self) -> MixedContentForVerbatim:
        """Build and return MixedContentForVerbatim object.

        Returns:
            MixedContentForVerbatim instance
        """
        # TODO: Add validation
        return self._obj
