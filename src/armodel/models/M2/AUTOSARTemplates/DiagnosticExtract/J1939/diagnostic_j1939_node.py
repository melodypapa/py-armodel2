"""DiagnosticJ1939Node AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Node."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "nm_node": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=J1939NmNode,
        ),  # nmNode
    }

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Node."""
        super().__init__()
        self.nm_node: Optional[J1939NmNode] = None


class DiagnosticJ1939NodeBuilder:
    """Builder for DiagnosticJ1939Node."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Node = DiagnosticJ1939Node()

    def build(self) -> DiagnosticJ1939Node:
        """Build and return DiagnosticJ1939Node object.

        Returns:
            DiagnosticJ1939Node instance
        """
        # TODO: Add validation
        return self._obj
