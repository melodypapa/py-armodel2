"""CryptoServiceCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 565)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoCertificateFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceCertificate(ARElement):
    """AUTOSAR CryptoServiceCertificate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    algorithm_family: Optional[Any]
    format: Optional[CryptoCertificateFormatEnum]
    maximum: Optional[PositiveInteger]
    next_higher: Optional[Any]
    server_name: Optional[String]
    def __init__(self) -> None:
        """Initialize CryptoServiceCertificate."""
        super().__init__()
        self.algorithm_family: Optional[Any] = None
        self.format: Optional[CryptoCertificateFormatEnum] = None
        self.maximum: Optional[PositiveInteger] = None
        self.next_higher: Optional[Any] = None
        self.server_name: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceCertificate":
        """Deserialize XML element to CryptoServiceCertificate object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceCertificate object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceCertificate, cls).deserialize(element)

        # Parse algorithm_family
        child = ARObject._find_child_element(element, "ALGORITHM-FAMILY")
        if child is not None:
            algorithm_family_value = child.text
            obj.algorithm_family = algorithm_family_value

        # Parse format
        child = ARObject._find_child_element(element, "FORMAT")
        if child is not None:
            format_value = CryptoCertificateFormatEnum.deserialize(child)
            obj.format = format_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse next_higher
        child = ARObject._find_child_element(element, "NEXT-HIGHER")
        if child is not None:
            next_higher_value = child.text
            obj.next_higher = next_higher_value

        # Parse server_name
        child = ARObject._find_child_element(element, "SERVER-NAME")
        if child is not None:
            server_name_value = child.text
            obj.server_name = server_name_value

        return obj



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
