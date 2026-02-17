"""EthTSynCrcFlags AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 868)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynCrcFlags(ARObject):
    """AUTOSAR EthTSynCrcFlags."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "crc_correction": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcCorrection
        "crc_domain": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcDomain
        "crc_message": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcMessage
        "crc_precise": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcPrecise
        "crc_sequence_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcSequenceId
        "crc_source_port": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcSourcePort
    }

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
