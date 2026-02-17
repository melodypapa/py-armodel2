"""LVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 347)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class LVerbatim(ARObject):
    """AUTOSAR LVerbatim."""

    def __init__(self) -> None:
        """Initialize LVerbatim."""
        super().__init__()


class LVerbatimBuilder:
    """Builder for LVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LVerbatim = LVerbatim()

    def build(self) -> LVerbatim:
        """Build and return LVerbatim object.

        Returns:
            LVerbatim instance
        """
        # TODO: Add validation
        return self._obj
