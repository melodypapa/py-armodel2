"""IEEE1722TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpConnection(ARElement):
    """AUTOSAR IEEE1722TpConnection."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_mac": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # destinationMac
        "mac_address_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macAddressString
        "pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # pdu
        "unique_stream_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # uniqueStreamId
        "version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # version
        "vlan_priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vlanPriority
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpConnection."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.mac_address_string: Optional[MacAddressString] = None
        self.pdu: Optional[PduTriggering] = None
        self.unique_stream_id: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None


class IEEE1722TpConnectionBuilder:
    """Builder for IEEE1722TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpConnection = IEEE1722TpConnection()

    def build(self) -> IEEE1722TpConnection:
        """Build and return IEEE1722TpConnection object.

        Returns:
            IEEE1722TpConnection instance
        """
        # TODO: Add validation
        return self._obj
