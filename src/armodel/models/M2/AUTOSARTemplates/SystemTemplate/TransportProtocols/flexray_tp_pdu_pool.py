"""FlexrayTpPduPool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayTpPduPool(Identifiable):
    """AUTOSAR FlexrayTpPduPool."""

    n_pdus: list[NPdu]
    def __init__(self) -> None:
        """Initialize FlexrayTpPduPool."""
        super().__init__()
        self.n_pdus: list[NPdu] = []


class FlexrayTpPduPoolBuilder:
    """Builder for FlexrayTpPduPool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpPduPool = FlexrayTpPduPool()

    def build(self) -> FlexrayTpPduPool:
        """Build and return FlexrayTpPduPool object.

        Returns:
            FlexrayTpPduPool instance
        """
        # TODO: Add validation
        return self._obj
