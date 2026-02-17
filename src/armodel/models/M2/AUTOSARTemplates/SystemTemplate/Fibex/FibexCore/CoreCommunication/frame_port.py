"""FramePort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)


class FramePort(CommConnectorPort):
    """AUTOSAR FramePort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize FramePort."""
        super().__init__()


class FramePortBuilder:
    """Builder for FramePort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePort = FramePort()

    def build(self) -> FramePort:
        """Build and return FramePort object.

        Returns:
            FramePort instance
        """
        # TODO: Add validation
        return self._obj
