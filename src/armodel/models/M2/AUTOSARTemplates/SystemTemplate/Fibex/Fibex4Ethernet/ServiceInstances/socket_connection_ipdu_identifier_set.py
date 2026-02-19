"""SocketConnectionIpduIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 490)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class SocketConnectionIpduIdentifierSet(FibexElement):
    """AUTOSAR SocketConnectionIpduIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_identifiers: list[SoConIPduIdentifier]
    def __init__(self) -> None:
        """Initialize SocketConnectionIpduIdentifierSet."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnectionIpduIdentifierSet":
        """Deserialize XML element to SocketConnectionIpduIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnectionIpduIdentifierSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse i_pdu_identifiers (list)
        obj.i_pdu_identifiers = []
        for child in ARObject._find_all_child_elements(element, "I-PDU-IDENTIFIERS"):
            i_pdu_identifiers_value = ARObject._deserialize_by_tag(child, "SoConIPduIdentifier")
            obj.i_pdu_identifiers.append(i_pdu_identifiers_value)

        return obj



class SocketConnectionIpduIdentifierSetBuilder:
    """Builder for SocketConnectionIpduIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnectionIpduIdentifierSet = SocketConnectionIpduIdentifierSet()

    def build(self) -> SocketConnectionIpduIdentifierSet:
        """Build and return SocketConnectionIpduIdentifierSet object.

        Returns:
            SocketConnectionIpduIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
