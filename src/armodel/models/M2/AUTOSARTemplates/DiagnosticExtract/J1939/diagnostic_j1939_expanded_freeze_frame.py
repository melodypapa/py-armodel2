"""DiagnosticJ1939ExpandedFreezeFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)


class DiagnosticJ1939ExpandedFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939ExpandedFreezeFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("node", None, False, False, DiagnosticJ1939Node),  # node
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939ExpandedFreezeFrame."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticJ1939ExpandedFreezeFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939ExpandedFreezeFrame":
        """Create DiagnosticJ1939ExpandedFreezeFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticJ1939ExpandedFreezeFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticJ1939ExpandedFreezeFrame since parent returns ARObject
        return cast("DiagnosticJ1939ExpandedFreezeFrame", obj)


class DiagnosticJ1939ExpandedFreezeFrameBuilder:
    """Builder for DiagnosticJ1939ExpandedFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939ExpandedFreezeFrame = DiagnosticJ1939ExpandedFreezeFrame()

    def build(self) -> DiagnosticJ1939ExpandedFreezeFrame:
        """Build and return DiagnosticJ1939ExpandedFreezeFrame object.

        Returns:
            DiagnosticJ1939ExpandedFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
