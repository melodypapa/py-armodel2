"""UserDefinedPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class UserDefinedPhysicalChannel(PhysicalChannel):
    """AUTOSAR UserDefinedPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedPhysicalChannel."""
        super().__init__()


class UserDefinedPhysicalChannelBuilder:
    """Builder for UserDefinedPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPhysicalChannel = UserDefinedPhysicalChannel()

    def build(self) -> UserDefinedPhysicalChannel:
        """Build and return UserDefinedPhysicalChannel object.

        Returns:
            UserDefinedPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
