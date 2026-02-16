"""DiagnosticJ1939Node AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)


class DiagnosticJ1939Node(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Node."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nm_node", None, False, False, J1939NmNode),  # nmNode
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Node."""
        super().__init__()
        self.nm_node: Optional[J1939NmNode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticJ1939Node to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Node":
        """Create DiagnosticJ1939Node from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticJ1939Node instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticJ1939Node since parent returns ARObject
        return cast("DiagnosticJ1939Node", obj)


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
