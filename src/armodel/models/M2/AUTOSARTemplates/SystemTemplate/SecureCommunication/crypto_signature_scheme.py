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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoSignatureScheme":
        """Deserialize XML element to CryptoSignatureScheme object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoSignatureScheme object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoSignatureScheme, cls).deserialize(element)

        # Parse signature
        child = ARObject._find_child_element(element, "SIGNATURE")
        if child is not None:
            signature_value = child.text
            obj.signature = signature_value

        return obj



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
