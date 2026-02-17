"""J1939TpPg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 625)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpPg(ARObject):
    """AUTOSAR J1939TpPg."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "direct_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NPdu,
        ),  # directPdu
        "pgn": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pgn
        "requestable": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # requestable
        "sdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IPdu,
        ),  # sdus
    }

    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu: Optional[NPdu] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdus: list[IPdu] = []


class J1939TpPgBuilder:
    """Builder for J1939TpPg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpPg = J1939TpPg()

    def build(self) -> J1939TpPg:
        """Build and return J1939TpPg object.

        Returns:
            J1939TpPg instance
        """
        # TODO: Add validation
        return self._obj
