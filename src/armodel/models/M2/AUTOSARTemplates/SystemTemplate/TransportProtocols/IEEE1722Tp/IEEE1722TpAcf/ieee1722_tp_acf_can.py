"""IEEE1722TpAcfCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    message_type_message_type_enum: Optional[IEEE1722TpAcfCan]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCan."""
        super().__init__()
        self.message_type_message_type_enum: Optional[IEEE1722TpAcfCan] = None


class IEEE1722TpAcfCanBuilder:
    """Builder for IEEE1722TpAcfCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCan = IEEE1722TpAcfCan()

    def build(self) -> IEEE1722TpAcfCan:
        """Build and return IEEE1722TpAcfCan object.

        Returns:
            IEEE1722TpAcfCan instance
        """
        # TODO: Add validation
        return self._obj
