"""MultilanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 75)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class MultilanguageReferrable(Referrable):
    """AUTOSAR MultilanguageReferrable."""
    """Abstract base class - do not instantiate directly."""

    long_name: Optional[MultilanguageLongName]
    def __init__(self) -> None:
        """Initialize MultilanguageReferrable."""
        super().__init__()
        self.long_name: Optional[MultilanguageLongName] = None


class MultilanguageReferrableBuilder:
    """Builder for MultilanguageReferrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageReferrable = MultilanguageReferrable()

    def build(self) -> MultilanguageReferrable:
        """Build and return MultilanguageReferrable object.

        Returns:
            MultilanguageReferrable instance
        """
        # TODO: Add validation
        return self._obj
