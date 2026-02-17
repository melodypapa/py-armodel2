"""CryptoServicePrimitive AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 376)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class CryptoServicePrimitive(ARElement):
    """AUTOSAR CryptoServicePrimitive."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "algorithm_family": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithmFamily
        "algorithm_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithmMode
        "algorithm": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithm
    }

    def __init__(self) -> None:
        """Initialize CryptoServicePrimitive."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.algorithm: Optional[String] = None


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
