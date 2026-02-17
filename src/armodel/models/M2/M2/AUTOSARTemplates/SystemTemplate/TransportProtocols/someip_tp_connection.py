"""SomeipTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)


class SomeipTpConnection(ARObject):
    """AUTOSAR SomeipTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SomeipTpChannel,
        ),  # tpChannel
        "tp_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # tpSdu
        "transport_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # transportPdu
    }

    def __init__(self) -> None:
        """Initialize SomeipTpConnection."""
        super().__init__()
        self.tp_channel: Optional[SomeipTpChannel] = None
        self.tp_sdu: Optional[PduTriggering] = None
        self.transport_pdu: Optional[PduTriggering] = None


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
