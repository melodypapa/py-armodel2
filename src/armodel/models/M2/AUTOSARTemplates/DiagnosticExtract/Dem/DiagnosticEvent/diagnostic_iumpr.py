"""DiagnosticIumpr AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticIumpr(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumpr."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event", None, False, False, DiagnosticEvent),  # event
        ("ratio_kind", None, False, False, DiagnosticIumprKindEnum),  # ratioKind
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIumpr."""
        super().__init__()
        self.event: Optional[DiagnosticEvent] = None
        self.ratio_kind: Optional[DiagnosticIumprKindEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIumpr to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumpr":
        """Create DiagnosticIumpr from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIumpr instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIumpr since parent returns ARObject
        return cast("DiagnosticIumpr", obj)


class DiagnosticIumprBuilder:
    """Builder for DiagnosticIumpr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumpr = DiagnosticIumpr()

    def build(self) -> DiagnosticIumpr:
        """Build and return DiagnosticIumpr object.

        Returns:
            DiagnosticIumpr instance
        """
        # TODO: Add validation
        return self._obj
