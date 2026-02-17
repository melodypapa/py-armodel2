"""IEEE1722TpAafConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 642)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpAafConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "aaf_aes3_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IEEE1722TpAafAes3DataTypeEnum,
        ),  # aafAes3Data
        "aaf_format_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IEEE1722TpAafFormatEnum,
        ),  # aafFormatEnum
        "aaf_nominal_rate": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # aafNominalRate
        "aes3_data_type_h": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # aes3DataTypeH
        "aes3_data_type_l": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # aes3DataTypeL
        "channels_per": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # channelsPer
        "event_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # eventDefault
        "pcm_bit_depth": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pcmBitDepth
        "sparse": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sparse
        "streams_per": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # streamsPer
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAafConnection."""
        super().__init__()
        self.aaf_aes3_data: Optional[IEEE1722TpAafAes3DataTypeEnum] = None
        self.aaf_format_enum: Optional[IEEE1722TpAafFormatEnum] = None
        self.aaf_nominal_rate: Optional[Any] = None
        self.aes3_data_type_h: Optional[PositiveInteger] = None
        self.aes3_data_type_l: Optional[PositiveInteger] = None
        self.channels_per: Optional[PositiveInteger] = None
        self.event_default: Optional[PositiveInteger] = None
        self.pcm_bit_depth: Optional[PositiveInteger] = None
        self.sparse: Optional[Boolean] = None
        self.streams_per: Optional[PositiveInteger] = None


class IEEE1722TpAafConnectionBuilder:
    """Builder for IEEE1722TpAafConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAafConnection = IEEE1722TpAafConnection()

    def build(self) -> IEEE1722TpAafConnection:
        """Build and return IEEE1722TpAafConnection object.

        Returns:
            IEEE1722TpAafConnection instance
        """
        # TODO: Add validation
        return self._obj
