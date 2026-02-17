"""SomeipTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SomeipTpChannel(Identifiable):
    """AUTOSAR SomeipTpChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "burst_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # burstSize
        "rx_timeout_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rxTimeoutTime
        "separation_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # separationTime
    }

    def __init__(self) -> None:
        """Initialize SomeipTpChannel."""
        super().__init__()
        self.burst_size: Optional[PositiveInteger] = None
        self.rx_timeout_time: Optional[TimeValue] = None
        self.separation_time: Optional[TimeValue] = None


class SomeipTpChannelBuilder:
    """Builder for SomeipTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpChannel = SomeipTpChannel()

    def build(self) -> SomeipTpChannel:
        """Build and return SomeipTpChannel object.

        Returns:
            SomeipTpChannel instance
        """
        # TODO: Add validation
        return self._obj
