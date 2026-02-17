"""CanPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_physical_channel import (
    AbstractCanPhysicalChannel,
)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """AUTOSAR CanPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize CanPhysicalChannel."""
        super().__init__()


class CanPhysicalChannelBuilder:
    """Builder for CanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanPhysicalChannel = CanPhysicalChannel()

    def build(self) -> CanPhysicalChannel:
        """Build and return CanPhysicalChannel object.

        Returns:
            CanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
