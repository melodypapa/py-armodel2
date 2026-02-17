"""CryptoServiceCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 565)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoCertificateFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceCertificate(ARElement):
    """AUTOSAR CryptoServiceCertificate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "algorithm_family": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoCertificate),
        ),  # algorithmFamily
        "format": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoCertificateFormatEnum,
        ),  # format
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximum
        "next_higher": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoService),
        ),  # nextHigher
        "server_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # serverName
    }

    def __init__(self) -> None:
        """Initialize CryptoServiceCertificate."""
        super().__init__()
        self.algorithm_family: Optional[Any] = None
        self.format: Optional[CryptoCertificateFormatEnum] = None
        self.maximum: Optional[PositiveInteger] = None
        self.next_higher: Optional[Any] = None
        self.server_name: Optional[String] = None


class CryptoServiceCertificateBuilder:
    """Builder for CryptoServiceCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceCertificate = CryptoServiceCertificate()

    def build(self) -> CryptoServiceCertificate:
        """Build and return CryptoServiceCertificate object.

        Returns:
            CryptoServiceCertificate instance
        """
        # TODO: Add validation
        return self._obj
