"""CanTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 611)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)


class CanTpNode(Identifiable):
    """AUTOSAR CanTpNode."""

    connector: Optional[Any]
    max_fc_wait: Optional[Integer]
    st_min: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    tp_address: Optional[CanTpAddress]
    def __init__(self) -> None:
        """Initialize CanTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.max_fc_wait: Optional[Integer] = None
        self.st_min: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.tp_address: Optional[CanTpAddress] = None


class CanTpNodeBuilder:
    """Builder for CanTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpNode = CanTpNode()

    def build(self) -> CanTpNode:
        """Build and return CanTpNode object.

        Returns:
            CanTpNode instance
        """
        # TODO: Add validation
        return self._obj
