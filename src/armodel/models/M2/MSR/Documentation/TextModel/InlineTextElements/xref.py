"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class Xref(ARObject):
    """AUTOSAR Xref."""

    label1: Optional[SingleLanguageLongName]
    referrable: Optional[Referrable]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable: Optional[Referrable] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None


class XrefBuilder:
    """Builder for Xref."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xref = Xref()

    def build(self) -> Xref:
        """Build and return Xref object.

        Returns:
            Xref instance
        """
        # TODO: Add validation
        return self._obj
