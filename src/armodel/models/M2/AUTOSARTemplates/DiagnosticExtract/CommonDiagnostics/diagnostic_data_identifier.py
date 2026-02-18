"""DiagnosticDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)


class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """AUTOSAR DiagnosticDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_elements: list[DiagnosticParameter]
    did_size: Optional[PositiveInteger]
    represents_vin: Optional[Boolean]
    support_info_byte: Optional[DiagnosticSupportInfoByte]
    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.did_size: Optional[PositiveInteger] = None
        self.represents_vin: Optional[Boolean] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None


class DiagnosticDataIdentifierBuilder:
    """Builder for DiagnosticDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataIdentifier = DiagnosticDataIdentifier()

    def build(self) -> DiagnosticDataIdentifier:
        """Build and return DiagnosticDataIdentifier object.

        Returns:
            DiagnosticDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
