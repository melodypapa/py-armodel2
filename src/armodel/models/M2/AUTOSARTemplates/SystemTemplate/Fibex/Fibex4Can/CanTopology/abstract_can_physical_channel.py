"""AbstractCanPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class AbstractCanPhysicalChannel(PhysicalChannel):
    """AUTOSAR AbstractCanPhysicalChannel."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize AbstractCanPhysicalChannel."""
        super().__init__()


class AbstractCanPhysicalChannelBuilder:
    """Builder for AbstractCanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanPhysicalChannel = AbstractCanPhysicalChannel()

    def build(self) -> AbstractCanPhysicalChannel:
        """Build and return AbstractCanPhysicalChannel object.

        Returns:
            AbstractCanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
