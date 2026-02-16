"""J1939TpPg AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direct_pdu", None, False, False, NPdu),  # directPdu
        ("pgn", None, True, False, None),  # pgn
        ("requestable", None, True, False, None),  # requestable
        ("sdus", None, False, True, IPdu),  # sdus
    ]

    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu: Optional[NPdu] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdus: list[IPdu] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939TpPg to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpPg":
        """Create J1939TpPg from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939TpPg instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939TpPg since parent returns ARObject
        return cast("J1939TpPg", obj)


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
