"""CryptoEllipticCurveProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoEllipticCurveProps(ARElement):
    """AUTOSAR CryptoEllipticCurveProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("named_curve_id", None, True, False, None),  # namedCurveId
    ]

    def __init__(self) -> None:
        """Initialize CryptoEllipticCurveProps."""
        super().__init__()
        self.named_curve_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoEllipticCurveProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoEllipticCurveProps":
        """Create CryptoEllipticCurveProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoEllipticCurveProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoEllipticCurveProps since parent returns ARObject
        return cast("CryptoEllipticCurveProps", obj)


class CryptoEllipticCurvePropsBuilder:
    """Builder for CryptoEllipticCurveProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoEllipticCurveProps = CryptoEllipticCurveProps()

    def build(self) -> CryptoEllipticCurveProps:
        """Build and return CryptoEllipticCurveProps object.

        Returns:
            CryptoEllipticCurveProps instance
        """
        # TODO: Add validation
        return self._obj
