"""EthTSynCrcFlags AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 868)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynCrcFlags(ARObject):
    """AUTOSAR EthTSynCrcFlags."""

    crc_correction: Optional[Boolean]
    crc_domain: Optional[Boolean]
    crc_message: Optional[Boolean]
    crc_precise: Optional[Boolean]
    crc_sequence_id: Optional[Boolean]
    crc_source_port: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthTSynCrcFlags."""
        super().__init__()
        self.crc_correction: Optional[Boolean] = None
        self.crc_domain: Optional[Boolean] = None
        self.crc_message: Optional[Boolean] = None
        self.crc_precise: Optional[Boolean] = None
        self.crc_sequence_id: Optional[Boolean] = None
        self.crc_source_port: Optional[Boolean] = None


class EthTSynCrcFlagsBuilder:
    """Builder for EthTSynCrcFlags."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTSynCrcFlags = EthTSynCrcFlags()

    def build(self) -> EthTSynCrcFlags:
        """Build and return EthTSynCrcFlags object.

        Returns:
            EthTSynCrcFlags instance
        """
        # TODO: Add validation
        return self._obj
