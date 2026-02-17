"""IEEE1722TpIidcConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 648)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "iidc_channel": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcChannel
        "iidc_data_block": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcDataBlock
        "iidc_fraction": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcFraction
        "iidc_source": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcSource
        "iidc_stream": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcStream
        "iidc_sy": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcSy
        "iidc_tag": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcTag
        "iidc_t_code": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # iidcTCode
    }

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
