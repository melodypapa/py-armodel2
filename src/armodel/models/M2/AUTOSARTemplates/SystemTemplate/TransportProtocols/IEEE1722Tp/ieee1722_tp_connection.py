"""IEEE1722TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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
from abc import ABC, abstractmethod


class IEEE1722TpConnection(ARElement, ABC):
    """AUTOSAR IEEE1722TpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    destination_mac: Optional[MacAddressString]
    mac_address_string: Optional[MacAddressString]
    pdu: Optional[PduTriggering]
    unique_stream_id: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    vlan_priority: Optional[PositiveInteger]
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
