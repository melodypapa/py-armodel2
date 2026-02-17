"""ScaleConstr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Limit,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class ScaleConstr(ARObject):
    """AUTOSAR ScaleConstr."""

    def __init__(self) -> None:
        """Initialize ScaleConstr."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.short_label: Optional[Identifier] = None
        self.upper_limit: Optional[Limit] = None
        self.validity: Optional[Any] = None


class ScaleConstrBuilder:
    """Builder for ScaleConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ScaleConstr = ScaleConstr()

    def build(self) -> ScaleConstr:
        """Build and return ScaleConstr object.

        Returns:
            ScaleConstr instance
        """
        # TODO: Add validation
        return self._obj
