"""LinSporadicFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinSporadicFrame(LinFrame):
    """AUTOSAR LinSporadicFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "substituteds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinUnconditionalFrame,
        ),  # substituteds
    }

    def __init__(self) -> None:
        """Initialize LinSporadicFrame."""
        super().__init__()
        self.substituteds: list[LinUnconditionalFrame] = []


class LinSporadicFrameBuilder:
    """Builder for LinSporadicFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSporadicFrame = LinSporadicFrame()

    def build(self) -> LinSporadicFrame:
        """Build and return LinSporadicFrame object.

        Returns:
            LinSporadicFrame instance
        """
        # TODO: Add validation
        return self._obj
