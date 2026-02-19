"""DiagnosticJ1939Node AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Node."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_node: Optional[J1939NmNode]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Node."""
        super().__init__()
        self.nm_node: Optional[J1939NmNode] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Node":
        """Deserialize XML element to DiagnosticJ1939Node object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939Node object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939Node, cls).deserialize(element)

        # Parse nm_node
        child = ARObject._find_child_element(element, "NM-NODE")
        if child is not None:
            nm_node_value = ARObject._deserialize_by_tag(child, "J1939NmNode")
            obj.nm_node = nm_node_value

        return obj



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
