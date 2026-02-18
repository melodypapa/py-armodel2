"""Gateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 837)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
    FrameMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
    IPduMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
    ISignalMapping,
)


class Gateway(FibexElement):
    """AUTOSAR Gateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu: Optional[EcuInstance]
    frame_mappings: list[FrameMapping]
    i_pdu_mappings: list[IPduMapping]
    signal_mappings: list[ISignalMapping]
    def __init__(self) -> None:
        """Initialize Gateway."""
        super().__init__()
        self.ecu: Optional[EcuInstance] = None
        self.frame_mappings: list[FrameMapping] = []
        self.i_pdu_mappings: list[IPduMapping] = []
        self.signal_mappings: list[ISignalMapping] = []


class GatewayBuilder:
    """Builder for Gateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Gateway = Gateway()

    def build(self) -> Gateway:
        """Build and return Gateway object.

        Returns:
            Gateway instance
        """
        # TODO: Add validation
        return self._obj
