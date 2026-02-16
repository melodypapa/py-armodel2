"""CryptoServicePrimitive AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class CryptoServicePrimitive(ARElement):
    """AUTOSAR CryptoServicePrimitive."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("algorithm_family", None, True, False, None),  # algorithmFamily
        ("algorithm_mode", None, True, False, None),  # algorithmMode
        ("algorithm", None, True, False, None),  # algorithm
    ]

    def __init__(self) -> None:
        """Initialize CryptoServicePrimitive."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.algorithm: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoServicePrimitive to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServicePrimitive":
        """Create CryptoServicePrimitive from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoServicePrimitive instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoServicePrimitive since parent returns ARObject
        return cast("CryptoServicePrimitive", obj)


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
