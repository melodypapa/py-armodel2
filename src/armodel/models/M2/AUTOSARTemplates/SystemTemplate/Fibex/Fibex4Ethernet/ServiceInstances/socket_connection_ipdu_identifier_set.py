"""SocketConnectionIpduIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 490)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class SocketConnectionIpduIdentifierSet(FibexElement):
    """AUTOSAR SocketConnectionIpduIdentifierSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "i_pdu_identifiers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SoConIPduIdentifier,
        ),  # iPduIdentifiers
    }

    def __init__(self) -> None:
        """Initialize SocketConnectionIpduIdentifierSet."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []


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
