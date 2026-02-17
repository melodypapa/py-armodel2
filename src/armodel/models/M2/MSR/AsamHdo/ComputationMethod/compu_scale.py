"""CompuScale AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 387)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2011)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    Identifier,
    Limit,
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class CompuScale(ARObject):
    """AUTOSAR CompuScale."""

    a2l_display_text: Optional[String]
    compu_inverse: Optional[CompuConst]
    compu_scale_contents: Optional[CompuScaleContents]
    desc: Optional[MultiLanguageOverviewParagraph]
    lower_limit: Optional[Limit]
    mask: Optional[PositiveUnlimitedInteger]
    short_label: Optional[Identifier]
    symbol: Optional[CIdentifier]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize CompuScale."""
        super().__init__()
        self.a2l_display_text: Optional[String] = None
        self.compu_inverse: Optional[CompuConst] = None
        self.compu_scale_contents: Optional[CompuScaleContents] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.mask: Optional[PositiveUnlimitedInteger] = None
        self.short_label: Optional[Identifier] = None
        self.symbol: Optional[CIdentifier] = None
        self.upper_limit: Optional[Limit] = None


class CompuScaleBuilder:
    """Builder for CompuScale."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScale = CompuScale()

    def build(self) -> CompuScale:
        """Build and return CompuScale object.

        Returns:
            CompuScale instance
        """
        # TODO: Add validation
        return self._obj
