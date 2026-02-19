"""J1939TpPg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 625)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direct_pdu: Optional[NPdu]
    pgn: Optional[Integer]
    requestable: Optional[Boolean]
    sdus: list[IPdu]
    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu: Optional[NPdu] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdus: list[IPdu] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpPg":
        """Deserialize XML element to J1939TpPg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpPg object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse direct_pdu
        child = ARObject._find_child_element(element, "DIRECT-PDU")
        if child is not None:
            direct_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.direct_pdu = direct_pdu_value

        # Parse pgn
        child = ARObject._find_child_element(element, "PGN")
        if child is not None:
            pgn_value = child.text
            obj.pgn = pgn_value

        # Parse requestable
        child = ARObject._find_child_element(element, "REQUESTABLE")
        if child is not None:
            requestable_value = child.text
            obj.requestable = requestable_value

        # Parse sdus (list from container "SDUS")
        obj.sdus = []
        container = ARObject._find_child_element(element, "SDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdus.append(child_value)

        return obj



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
