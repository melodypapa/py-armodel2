"""DiagnosticJ1939FreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 220)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)


class DiagnosticJ1939FreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939FreezeFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "node": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticJ1939Node,
        ),  # node
    }

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939FreezeFrame."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None


class DiagnosticJ1939FreezeFrameBuilder:
    """Builder for DiagnosticJ1939FreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939FreezeFrame = DiagnosticJ1939FreezeFrame()

    def build(self) -> DiagnosticJ1939FreezeFrame:
        """Build and return DiagnosticJ1939FreezeFrame object.

        Returns:
            DiagnosticJ1939FreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
