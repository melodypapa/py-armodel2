"""DiagnosticTroubleCodeUdsToTroubleCodeObdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trouble_code: Optional[DiagnosticTroubleCode]
    trouble_code_uds: Optional[DiagnosticTroubleCode]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""
        super().__init__()
        self.trouble_code: Optional[DiagnosticTroubleCode] = None
        self.trouble_code_uds: Optional[DiagnosticTroubleCode] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """Deserialize XML element to DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse trouble_code
        child = ARObject._find_child_element(element, "TROUBLE-CODE")
        if child is not None:
            trouble_code_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.trouble_code = trouble_code_value

        # Parse trouble_code_uds
        child = ARObject._find_child_element(element, "TROUBLE-CODE-UDS")
        if child is not None:
            trouble_code_uds_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.trouble_code_uds = trouble_code_uds_value

        return obj



class DiagnosticTroubleCodeUdsToTroubleCodeObdMappingBuilder:
    """Builder for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUdsToTroubleCodeObdMapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping()

    def build(self) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """Build and return DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Returns:
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        # TODO: Add validation
        return self._obj
