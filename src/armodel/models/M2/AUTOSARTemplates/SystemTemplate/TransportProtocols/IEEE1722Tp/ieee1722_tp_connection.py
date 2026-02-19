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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    pdu_ref: Optional[ARRef]
    unique_stream_id: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    vlan_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpConnection."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.mac_address_string: Optional[MacAddressString] = None
        self.pdu_ref: Optional[ARRef] = None
        self.unique_stream_id: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConnection":
        """Deserialize XML element to IEEE1722TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpConnection, cls).deserialize(element)

        # Parse destination_mac
        child = ARObject._find_child_element(element, "DESTINATION-MAC")
        if child is not None:
            destination_mac_value = child.text
            obj.destination_mac = destination_mac_value

        # Parse mac_address_string
        child = ARObject._find_child_element(element, "MAC-ADDRESS-STRING")
        if child is not None:
            mac_address_string_value = child.text
            obj.mac_address_string = mac_address_string_value

        # Parse pdu_ref
        child = ARObject._find_child_element(element, "PDU")
        if child is not None:
            pdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_ref = pdu_ref_value

        # Parse unique_stream_id
        child = ARObject._find_child_element(element, "UNIQUE-STREAM-ID")
        if child is not None:
            unique_stream_id_value = child.text
            obj.unique_stream_id = unique_stream_id_value

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        # Parse vlan_priority
        child = ARObject._find_child_element(element, "VLAN-PRIORITY")
        if child is not None:
            vlan_priority_value = child.text
            obj.vlan_priority = vlan_priority_value

        return obj



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
