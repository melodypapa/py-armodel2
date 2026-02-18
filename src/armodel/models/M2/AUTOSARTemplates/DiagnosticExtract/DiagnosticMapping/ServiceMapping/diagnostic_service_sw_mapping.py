"""DiagnosticServiceSwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceSwMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_data: Optional[DataPrototype]
    diagnostic_data: Optional[DiagnosticDataElement]
    diagnostic: Optional[DiagnosticParameter]
    mapped_bsw: Optional[Any]
    mapped_flat_swc: Optional[Any]
    mapped_swc: Optional[Any]
    parameter: Optional[DiagnosticParameter]
    service_instance: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceSwMapping."""
        super().__init__()
        self.accessed_data: Optional[DataPrototype] = None
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
        self.diagnostic: Optional[DiagnosticParameter] = None
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None
        self.parameter: Optional[DiagnosticParameter] = None
        self.service_instance: Optional[Any] = None


class DiagnosticServiceSwMappingBuilder:
    """Builder for DiagnosticServiceSwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceSwMapping = DiagnosticServiceSwMapping()

    def build(self) -> DiagnosticServiceSwMapping:
        """Build and return DiagnosticServiceSwMapping object.

        Returns:
            DiagnosticServiceSwMapping instance
        """
        # TODO: Add validation
        return self._obj
