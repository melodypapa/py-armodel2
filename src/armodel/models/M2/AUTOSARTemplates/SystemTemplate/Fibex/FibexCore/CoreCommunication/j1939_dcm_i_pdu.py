"""J1939DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class J1939DcmIPdu(IPdu):
    """AUTOSAR J1939DcmIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # diagnostic
        "message_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (e.g),
        ),  # MessageType
    }

    def __init__(self) -> None:
        """Initialize J1939DcmIPdu."""
        super().__init__()
        self.diagnostic: Optional[PositiveInteger] = None
        self.message_type: Any = None


class J1939DcmIPduBuilder:
    """Builder for J1939DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939DcmIPdu = J1939DcmIPdu()

    def build(self) -> J1939DcmIPdu:
        """Build and return J1939DcmIPdu object.

        Returns:
            J1939DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
