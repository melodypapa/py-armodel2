"""ISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 994)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_timing import (
    IPduTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class ISignalIPdu(IPdu):
    """AUTOSAR ISignalIPdu."""

    def __init__(self) -> None:
        """Initialize ISignalIPdu."""
        super().__init__()
        self.i_pdu_timing: Optional[IPduTiming] = None
        self.i_signal_to_pdus: list[ISignalToIPduMapping] = []
        self.unused_bit: Optional[Integer] = None


class ISignalIPduBuilder:
    """Builder for ISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPdu = ISignalIPdu()

    def build(self) -> ISignalIPdu:
        """Build and return ISignalIPdu object.

        Returns:
            ISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
