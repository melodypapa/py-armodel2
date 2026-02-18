"""MixedContentForUnitNames AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 456)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from abc import ABC, abstractmethod


class MixedContentForUnitNames(ARObject, ABC):
    """AUTOSAR MixedContentForUnitNames."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    sub: Superscript
    sup: Superscript
    def __init__(self) -> None:
        """Initialize MixedContentForUnitNames."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None


class MixedContentForUnitNamesBuilder:
    """Builder for MixedContentForUnitNames."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForUnitNames = MixedContentForUnitNames()

    def build(self) -> MixedContentForUnitNames:
        """Build and return MixedContentForUnitNames object.

        Returns:
            MixedContentForUnitNames instance
        """
        # TODO: Add validation
        return self._obj
