"""LinFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 428)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class LinFrame(Frame):
    """AUTOSAR LinFrame."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize LinFrame."""
        super().__init__()


class LinFrameBuilder:
    """Builder for LinFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrame = LinFrame()

    def build(self) -> LinFrame:
        """Build and return LinFrame object.

        Returns:
            LinFrame instance
        """
        # TODO: Add validation
        return self._obj
