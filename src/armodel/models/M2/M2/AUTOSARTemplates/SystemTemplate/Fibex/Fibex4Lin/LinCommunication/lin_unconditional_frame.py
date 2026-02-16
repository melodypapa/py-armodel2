"""LinUnconditionalFrame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinUnconditionalFrame(LinFrame):
    """AUTOSAR LinUnconditionalFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize LinUnconditionalFrame."""
        super().__init__()


class LinUnconditionalFrameBuilder:
    """Builder for LinUnconditionalFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinUnconditionalFrame = LinUnconditionalFrame()

    def build(self) -> LinUnconditionalFrame:
        """Build and return LinUnconditionalFrame object.

        Returns:
            LinUnconditionalFrame instance
        """
        # TODO: Add validation
        return self._obj
