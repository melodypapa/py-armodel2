"""DoIpTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DoIpTpConnection(TpConnection):
    """AUTOSAR DoIpTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_source: Optional[DoIpLogicAddress]
    do_ip_target: Optional[DoIpLogicAddress]
    tp_sdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DoIpTpConnection."""
        super().__init__()
        self.do_ip_source: Optional[DoIpLogicAddress] = None
        self.do_ip_target: Optional[DoIpLogicAddress] = None
        self.tp_sdu_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConnection":
        """Deserialize XML element to DoIpTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse do_ip_source
        child = ARObject._find_child_element(element, "DO-IP-SOURCE")
        if child is not None:
            do_ip_source_value = ARObject._deserialize_by_tag(child, "DoIpLogicAddress")
            obj.do_ip_source = do_ip_source_value

        # Parse do_ip_target
        child = ARObject._find_child_element(element, "DO-IP-TARGET")
        if child is not None:
            do_ip_target_value = ARObject._deserialize_by_tag(child, "DoIpLogicAddress")
            obj.do_ip_target = do_ip_target_value

        # Parse tp_sdu_ref
        child = ARObject._find_child_element(element, "TP-SDU")
        if child is not None:
            tp_sdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.tp_sdu_ref = tp_sdu_ref_value

        return obj



class DoIpTpConnectionBuilder:
    """Builder for DoIpTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConnection = DoIpTpConnection()

    def build(self) -> DoIpTpConnection:
        """Build and return DoIpTpConnection object.

        Returns:
            DoIpTpConnection instance
        """
        # TODO: Add validation
        return self._obj
