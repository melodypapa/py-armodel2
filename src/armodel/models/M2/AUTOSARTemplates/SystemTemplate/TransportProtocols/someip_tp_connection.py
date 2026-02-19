"""SomeipTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)


class SomeipTpConnection(ARObject):
    """AUTOSAR SomeipTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_channel: Optional[SomeipTpChannel]
    tp_sdu_ref: Optional[ARRef]
    transport_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SomeipTpConnection."""
        super().__init__()
        self.tp_channel: Optional[SomeipTpChannel] = None
        self.tp_sdu_ref: Optional[ARRef] = None
        self.transport_pdu_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConnection":
        """Deserialize XML element to SomeipTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_channel
        child = ARObject._find_child_element(element, "TP-CHANNEL")
        if child is not None:
            tp_channel_value = ARObject._deserialize_by_tag(child, "SomeipTpChannel")
            obj.tp_channel = tp_channel_value

        # Parse tp_sdu_ref
        child = ARObject._find_child_element(element, "TP-SDU")
        if child is not None:
            tp_sdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.tp_sdu_ref = tp_sdu_ref_value

        # Parse transport_pdu_ref
        child = ARObject._find_child_element(element, "TRANSPORT-PDU")
        if child is not None:
            transport_pdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.transport_pdu_ref = transport_pdu_ref_value

        return obj



class SomeipTpConnectionBuilder:
    """Builder for SomeipTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpConnection = SomeipTpConnection()

    def build(self) -> SomeipTpConnection:
        """Build and return SomeipTpConnection object.

        Returns:
            SomeipTpConnection instance
        """
        # TODO: Add validation
        return self._obj
