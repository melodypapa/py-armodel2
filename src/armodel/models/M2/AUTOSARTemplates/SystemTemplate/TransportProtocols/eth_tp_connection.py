"""EthTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 618)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class EthTpConnection(TpConnection):
    """AUTOSAR EthTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EthTpConnection."""
        super().__init__()
        self.tp_sdu_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTpConnection":
        """Deserialize XML element to EthTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTpConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_sdu_refs (list)
        obj.tp_sdu_refs = []
        for child in ARObject._find_all_child_elements(element, "TP-SDUS"):
            tp_sdu_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.tp_sdu_refs.append(tp_sdu_refs_value)

        return obj



class EthTpConnectionBuilder:
    """Builder for EthTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConnection = EthTpConnection()

    def build(self) -> EthTpConnection:
        """Build and return EthTpConnection object.

        Returns:
            EthTpConnection instance
        """
        # TODO: Add validation
        return self._obj
