"""DiagnosticDemProvidedDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticDemProvidedDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element: Optional[DiagnosticDataElement]
    data_provider: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DiagnosticDemProvidedDataMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.data_provider: Optional[NameToken] = None


class DiagnosticDemProvidedDataMappingBuilder:
    """Builder for DiagnosticDemProvidedDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDemProvidedDataMapping = DiagnosticDemProvidedDataMapping()

    def build(self) -> DiagnosticDemProvidedDataMapping:
        """Build and return DiagnosticDemProvidedDataMapping object.

        Returns:
            DiagnosticDemProvidedDataMapping instance
        """
        # TODO: Add validation
        return self._obj
