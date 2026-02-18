"""Referrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 63)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1002)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2049)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 31)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
    ShortNameFragment,
)
from abc import ABC, abstractmethod


class Referrable(ARObject, ABC):
    """AUTOSAR Referrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    short_name: Identifier
    short_name_fragments: list[ShortNameFragment]
    def __init__(self) -> None:
        """Initialize Referrable."""
        super().__init__()
        self.short_name: Identifier = None
        self.short_name_fragments: list[ShortNameFragment] = []


class ReferrableBuilder:
    """Builder for Referrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Referrable = Referrable()

    def build(self) -> Referrable:
        """Build and return Referrable object.

        Returns:
            Referrable instance
        """
        # TODO: Add validation
        return self._obj
