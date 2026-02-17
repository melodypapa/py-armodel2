"""Baseline AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_defs: list[SdgDef] = []
        self.customs: list[Documentation] = []
        self.standards: list[String] = []


class BaselineBuilder:
    """Builder for Baseline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Baseline = Baseline()

    def build(self) -> Baseline:
        """Build and return Baseline object.

        Returns:
            Baseline instance
        """
        # TODO: Add validation
        return self._obj
