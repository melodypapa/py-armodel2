"""Ieee1722TpEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 579)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722TpEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR Ieee1722TpEthernetFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "relative": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # relative
        "stream_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # streamIdentifier
        "sub_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # subType
        "version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # version
    }

    def __init__(self) -> None:
        """Initialize Ieee1722TpEthernetFrame."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None


class Ieee1722TpEthernetFrameBuilder:
    """Builder for Ieee1722TpEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722TpEthernetFrame = Ieee1722TpEthernetFrame()

    def build(self) -> Ieee1722TpEthernetFrame:
        """Build and return Ieee1722TpEthernetFrame object.

        Returns:
            Ieee1722TpEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
