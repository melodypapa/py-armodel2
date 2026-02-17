"""CryptoEllipticCurveProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 564)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoEllipticCurveProps(ARElement):
    """AUTOSAR CryptoEllipticCurveProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "named_curve_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # namedCurveId
    }

    def __init__(self) -> None:
        """Initialize CryptoEllipticCurveProps."""
        super().__init__()
        self.named_curve_id: Optional[PositiveInteger] = None


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
