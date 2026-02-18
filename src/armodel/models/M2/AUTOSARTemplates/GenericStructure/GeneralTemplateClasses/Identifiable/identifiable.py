"""Identifiable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 318)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 296)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 995)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2027)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 229)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 74)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 59)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 31)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    String,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from abc import ABC, abstractmethod


class Identifiable(MultilanguageReferrable, ABC):
    """AUTOSAR Identifiable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    admin_data: Optional[AdminData]
    annotations: list[Annotation]
    category: Optional[CategoryString]
    desc: Optional[MultiLanguageOverviewParagraph]
    introduction: Optional[DocumentationBlock]
    uuid: Optional[String]
    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.uuid: Optional[String] = None


class IdentifiableBuilder:
    """Builder for Identifiable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Identifiable = Identifiable()

    def build(self) -> Identifiable:
        """Build and return Identifiable object.

        Returns:
            Identifiable instance
        """
        # TODO: Add validation
        return self._obj
