"""CryptoServicePrimitive AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 376)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class CryptoServicePrimitive(ARElement):
    """AUTOSAR CryptoServicePrimitive."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    algorithm: Optional[String]
    def __init__(self) -> None:
        """Initialize CryptoServicePrimitive."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.algorithm: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServicePrimitive":
        """Deserialize XML element to CryptoServicePrimitive object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServicePrimitive object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServicePrimitive, cls).deserialize(element)

        # Parse algorithm_family
        child = ARObject._find_child_element(element, "ALGORITHM-FAMILY")
        if child is not None:
            algorithm_family_value = child.text
            obj.algorithm_family = algorithm_family_value

        # Parse algorithm_mode
        child = ARObject._find_child_element(element, "ALGORITHM-MODE")
        if child is not None:
            algorithm_mode_value = child.text
            obj.algorithm_mode = algorithm_mode_value

        # Parse algorithm
        child = ARObject._find_child_element(element, "ALGORITHM")
        if child is not None:
            algorithm_value = child.text
            obj.algorithm = algorithm_value

        return obj



class CryptoServicePrimitiveBuilder:
    """Builder for CryptoServicePrimitive."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServicePrimitive = CryptoServicePrimitive()

    def build(self) -> CryptoServicePrimitive:
        """Build and return CryptoServicePrimitive object.

        Returns:
            CryptoServicePrimitive instance
        """
        # TODO: Add validation
        return self._obj
