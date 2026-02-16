"""CryptoServiceKey AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class CryptoServiceKey(ARElement):
    """AUTOSAR CryptoServiceKey."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("algorithm_family", None, True, False, None),  # algorithmFamily
        ("development", None, False, False, ValueSpecification),  # development
        ("key_generation", None, False, False, CryptoServiceKey),  # keyGeneration
        ("key_storage_type", None, True, False, None),  # keyStorageType
        ("length", None, True, False, None),  # length
    ]

    def __init__(self) -> None:
        """Initialize CryptoServiceKey."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.development: Optional[ValueSpecification] = None
        self.key_generation: Optional[CryptoServiceKey] = None
        self.key_storage_type: Optional[String] = None
        self.length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoServiceKey to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceKey":
        """Create CryptoServiceKey from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoServiceKey instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoServiceKey since parent returns ARObject
        return cast("CryptoServiceKey", obj)


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
