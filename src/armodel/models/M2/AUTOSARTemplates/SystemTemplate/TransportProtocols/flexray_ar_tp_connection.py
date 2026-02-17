"""FlexrayArTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 603)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpConnection(TpConnection):
    """AUTOSAR FlexrayArTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connection_prio": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # connectionPrio
        "direct_tp_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPdu,
        ),  # directTpSdu
        "multicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpAddress,
        ),  # multicast
        "reversed_tp_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPdu,
        ),  # reversedTpSdu
        "source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlexrayArTpNode,
        ),  # source
        "targets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayArTpNode,
        ),  # targets
    }

    def __init__(self) -> None:
        """Initialize FlexrayArTpConnection."""
        super().__init__()
        self.connection_prio: Optional[Integer] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.source: Optional[FlexrayArTpNode] = None
        self.targets: list[FlexrayArTpNode] = []


class FlexrayArTpConnectionBuilder:
    """Builder for FlexrayArTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpConnection = FlexrayArTpConnection()

    def build(self) -> FlexrayArTpConnection:
        """Build and return FlexrayArTpConnection object.

        Returns:
            FlexrayArTpConnection instance
        """
        # TODO: Add validation
        return self._obj
