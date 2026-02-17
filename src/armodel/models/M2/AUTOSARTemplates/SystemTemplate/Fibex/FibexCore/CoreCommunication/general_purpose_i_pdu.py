"""GeneralPurposeIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 345)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)


class GeneralPurposeIPdu(IPdu):
    """AUTOSAR GeneralPurposeIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize GeneralPurposeIPdu."""
        super().__init__()


class GeneralPurposeIPduBuilder:
    """Builder for GeneralPurposeIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeIPdu = GeneralPurposeIPdu()

    def build(self) -> GeneralPurposeIPdu:
        """Build and return GeneralPurposeIPdu object.

        Returns:
            GeneralPurposeIPdu instance
        """
        # TODO: Add validation
        return self._obj
