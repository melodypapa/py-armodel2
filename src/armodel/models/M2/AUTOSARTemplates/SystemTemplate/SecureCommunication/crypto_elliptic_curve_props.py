"""CryptoEllipticCurveProps AUTOSAR element.

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


class CryptoEllipticCurveProps(ARElement):
    """AUTOSAR CryptoEllipticCurveProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    named_curve_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoEllipticCurveProps."""
        super().__init__()
        self.named_curve_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoEllipticCurveProps":
        """Deserialize XML element to CryptoEllipticCurveProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoEllipticCurveProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse named_curve_id
        child = ARObject._find_child_element(element, "NAMED-CURVE-ID")
        if child is not None:
            named_curve_id_value = child.text
            obj.named_curve_id = named_curve_id_value

        return obj



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
