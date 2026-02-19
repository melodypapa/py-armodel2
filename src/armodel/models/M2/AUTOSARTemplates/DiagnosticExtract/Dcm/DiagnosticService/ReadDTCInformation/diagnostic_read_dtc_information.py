"""DiagnosticReadDTCInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDTCInformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformation."""
        super().__init__()
        self.read: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDTCInformation":
        """Deserialize XML element to DiagnosticReadDTCInformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDTCInformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDTCInformation, cls).deserialize(element)

        # Parse read
        child = ARObject._find_child_element(element, "READ")
        if child is not None:
            read_value = child.text
            obj.read = read_value

        return obj



class DiagnosticReadDTCInformationBuilder:
    """Builder for DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformation = DiagnosticReadDTCInformation()

    def build(self) -> DiagnosticReadDTCInformation:
        """Build and return DiagnosticReadDTCInformation object.

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # TODO: Add validation
        return self._obj
