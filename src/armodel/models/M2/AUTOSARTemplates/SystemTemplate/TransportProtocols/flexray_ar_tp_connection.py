"""FlexrayArTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 603)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_prio: Optional[Integer]
    direct_tp_sdu: Optional[IPdu]
    multicast: Optional[TpAddress]
    reversed_tp_sdu: Optional[IPdu]
    source: Optional[FlexrayArTpNode]
    targets: list[FlexrayArTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayArTpConnection."""
        super().__init__()
        self.connection_prio: Optional[Integer] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.source: Optional[FlexrayArTpNode] = None
        self.targets: list[FlexrayArTpNode] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConnection":
        """Deserialize XML element to FlexrayArTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse connection_prio
        child = ARObject._find_child_element(element, "CONNECTION-PRIO")
        if child is not None:
            connection_prio_value = child.text
            obj.connection_prio = connection_prio_value

        # Parse direct_tp_sdu
        child = ARObject._find_child_element(element, "DIRECT-TP-SDU")
        if child is not None:
            direct_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.direct_tp_sdu = direct_tp_sdu_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.multicast = multicast_value

        # Parse reversed_tp_sdu
        child = ARObject._find_child_element(element, "REVERSED-TP-SDU")
        if child is not None:
            reversed_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.reversed_tp_sdu = reversed_tp_sdu_value

        # Parse source
        child = ARObject._find_child_element(element, "SOURCE")
        if child is not None:
            source_value = ARObject._deserialize_by_tag(child, "FlexrayArTpNode")
            obj.source = source_value

        # Parse targets (list)
        obj.targets = []
        for child in ARObject._find_all_child_elements(element, "TARGETS"):
            targets_value = ARObject._deserialize_by_tag(child, "FlexrayArTpNode")
            obj.targets.append(targets_value)

        return obj



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
