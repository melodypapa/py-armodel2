"""IEEE1722TpIidcConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 648)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iidc_channel: Optional[PositiveInteger]
    iidc_data_block: Optional[PositiveInteger]
    iidc_fraction: Optional[PositiveInteger]
    iidc_source: Optional[Boolean]
    iidc_stream: Optional[PositiveInteger]
    iidc_sy: Optional[PositiveInteger]
    iidc_tag: Optional[PositiveInteger]
    iidc_t_code: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpIidcConnection."""
        super().__init__()
        self.iidc_channel: Optional[PositiveInteger] = None
        self.iidc_data_block: Optional[PositiveInteger] = None
        self.iidc_fraction: Optional[PositiveInteger] = None
        self.iidc_source: Optional[Boolean] = None
        self.iidc_stream: Optional[PositiveInteger] = None
        self.iidc_sy: Optional[PositiveInteger] = None
        self.iidc_tag: Optional[PositiveInteger] = None
        self.iidc_t_code: Optional[PositiveInteger] = None


class IEEE1722TpIidcConnectionBuilder:
    """Builder for IEEE1722TpIidcConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpIidcConnection = IEEE1722TpIidcConnection()

    def build(self) -> IEEE1722TpIidcConnection:
        """Build and return IEEE1722TpIidcConnection object.

        Returns:
            IEEE1722TpIidcConnection instance
        """
        # TODO: Add validation
        return self._obj
