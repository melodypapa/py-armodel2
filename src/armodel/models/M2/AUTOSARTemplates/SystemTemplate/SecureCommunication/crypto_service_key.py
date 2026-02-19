"""CryptoServiceKey AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 377)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 58)

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
    String,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class CryptoServiceKey(ARElement):
    """AUTOSAR CryptoServiceKey."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    algorithm_family: Optional[String]
    development: Optional[ValueSpecification]
    key_generation: Optional[CryptoServiceKey]
    key_storage_type: Optional[String]
    length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceKey."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.development: Optional[ValueSpecification] = None
        self.key_generation: Optional[CryptoServiceKey] = None
        self.key_storage_type: Optional[String] = None
        self.length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceKey":
        """Deserialize XML element to CryptoServiceKey object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceKey object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceKey, cls).deserialize(element)

        # Parse algorithm_family
        child = ARObject._find_child_element(element, "ALGORITHM-FAMILY")
        if child is not None:
            algorithm_family_value = child.text
            obj.algorithm_family = algorithm_family_value

        # Parse development
        child = ARObject._find_child_element(element, "DEVELOPMENT")
        if child is not None:
            development_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.development = development_value

        # Parse key_generation
        child = ARObject._find_child_element(element, "KEY-GENERATION")
        if child is not None:
            key_generation_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.key_generation = key_generation_value

        # Parse key_storage_type
        child = ARObject._find_child_element(element, "KEY-STORAGE-TYPE")
        if child is not None:
            key_storage_type_value = child.text
            obj.key_storage_type = key_storage_type_value

        # Parse length
        child = ARObject._find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        return obj



class CryptoServiceKeyBuilder:
    """Builder for CryptoServiceKey."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceKey = CryptoServiceKey()

    def build(self) -> CryptoServiceKey:
        """Build and return CryptoServiceKey object.

        Returns:
            CryptoServiceKey instance
        """
        # TODO: Add validation
        return self._obj
