"""DiagnosticAuthTransmitCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthTransmitCertificate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    certificates: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificate."""
        super().__init__()
        self.certificates: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificate":
        """Deserialize XML element to DiagnosticAuthTransmitCertificate object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthTransmitCertificate object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse certificates (list)
        obj.certificates = []
        for child in ARObject._find_all_child_elements(element, "CERTIFICATES"):
            certificates_value = child.text
            obj.certificates.append(certificates_value)

        return obj



class DiagnosticAuthTransmitCertificateBuilder:
    """Builder for DiagnosticAuthTransmitCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificate = DiagnosticAuthTransmitCertificate()

    def build(self) -> DiagnosticAuthTransmitCertificate:
        """Build and return DiagnosticAuthTransmitCertificate object.

        Returns:
            DiagnosticAuthTransmitCertificate instance
        """
        # TODO: Add validation
        return self._obj
