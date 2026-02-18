"""IEEE1722TpAvConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 639)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """AUTOSAR IEEE1722TpAvConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max_transit_time: Optional[TimeValue]
    sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAvConnection."""
        super().__init__()
        self.max_transit_time: Optional[TimeValue] = None
        self.sdu_refs: list[ARRef] = []


class IEEE1722TpAvConnectionBuilder:
    """Builder for IEEE1722TpAvConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAvConnection = IEEE1722TpAvConnection()

    def build(self) -> IEEE1722TpAvConnection:
        """Build and return IEEE1722TpAvConnection object.

        Returns:
            IEEE1722TpAvConnection instance
        """
        # TODO: Add validation
        return self._obj
