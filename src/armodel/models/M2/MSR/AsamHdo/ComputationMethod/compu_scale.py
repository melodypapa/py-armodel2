"""CompuScale AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 387)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2011)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "a2l_display_text": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # a2lDisplayText
        "compu_inverse": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuConst,
        ),  # compuInverse
        "compu_scale_contents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuScaleContents,
        ),  # compuScaleContents
        "desc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # desc
        "lower_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # lowerLimit
        "mask": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mask
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
        "upper_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperLimit
    }

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
