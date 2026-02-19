"""DiagnosticVerifyCertificateBidirectional AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticVerifyCertificateBidirectional(DiagnosticAuthentication):
    """AUTOSAR DiagnosticVerifyCertificateBidirectional."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticVerifyCertificateBidirectional."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticVerifyCertificateBidirectional":
        """Deserialize XML element to DiagnosticVerifyCertificateBidirectional object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticVerifyCertificateBidirectional object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticVerifyCertificateBidirectional, cls).deserialize(element)



class DiagnosticVerifyCertificateBidirectionalBuilder:
    """Builder for DiagnosticVerifyCertificateBidirectional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticVerifyCertificateBidirectional = DiagnosticVerifyCertificateBidirectional()

    def build(self) -> DiagnosticVerifyCertificateBidirectional:
        """Build and return DiagnosticVerifyCertificateBidirectional object.

        Returns:
            DiagnosticVerifyCertificateBidirectional instance
        """
        # TODO: Add validation
        return self._obj
