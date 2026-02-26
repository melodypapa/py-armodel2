"""Authentication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
        DiagnosticAuthentication,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication_class import (
        DiagnosticAuthenticationClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication_configuration import (
        DiagnosticAuthenticationConfiguration,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_verify_certificate_bidirectional import (
        DiagnosticVerifyCertificateBidirectional,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_verify_certificate_unidirectional import (
        DiagnosticVerifyCertificateUnidirectional,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_de_authentication import (
        DiagnosticDeAuthentication,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_proof_of_ownership import (
        DiagnosticProofOfOwnership,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_auth_transmit_certificate import (
        DiagnosticAuthTransmitCertificate,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_auth_transmit_certificate_evaluation import (
        DiagnosticAuthTransmitCertificateEvaluation,
    )

__all__ = [
    "DiagnosticAuthTransmitCertificate",
    "DiagnosticAuthTransmitCertificateEvaluation",
    "DiagnosticAuthentication",
    "DiagnosticAuthenticationClass",
    "DiagnosticAuthenticationConfiguration",
    "DiagnosticDeAuthentication",
    "DiagnosticProofOfOwnership",
    "DiagnosticVerifyCertificateBidirectional",
    "DiagnosticVerifyCertificateUnidirectional",
]
