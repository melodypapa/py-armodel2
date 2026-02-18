"""CryptoSignatureScheme AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 564)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoSignatureScheme(ARElement):
    """AUTOSAR CryptoSignatureScheme."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signature: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoSignatureScheme."""
        super().__init__()
        self.signature: Optional[PositiveInteger] = None


class CryptoSignatureSchemeBuilder:
    """Builder for CryptoSignatureScheme."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoSignatureScheme = CryptoSignatureScheme()

    def build(self) -> CryptoSignatureScheme:
        """Build and return CryptoSignatureScheme object.

        Returns:
            CryptoSignatureScheme instance
        """
        # TODO: Add validation
        return self._obj
