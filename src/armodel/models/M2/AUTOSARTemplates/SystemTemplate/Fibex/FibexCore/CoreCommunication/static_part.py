"""StaticPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 410)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class StaticPart(MultiplexedPart):
    """AUTOSAR StaticPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu: Optional[ISignalIPdu]
    def __init__(self) -> None:
        """Initialize StaticPart."""
        super().__init__()
        self.i_pdu: Optional[ISignalIPdu] = None


class StaticPartBuilder:
    """Builder for StaticPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticPart = StaticPart()

    def build(self) -> StaticPart:
        """Build and return StaticPart object.

        Returns:
            StaticPart instance
        """
        # TODO: Add validation
        return self._obj
