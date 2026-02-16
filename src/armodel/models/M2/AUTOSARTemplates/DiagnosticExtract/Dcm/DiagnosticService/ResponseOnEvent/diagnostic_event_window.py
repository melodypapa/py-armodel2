"""DiagnosticEventWindow AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
    DiagnosticEventWindow,
)


class DiagnosticEventWindow(ARObject):
    """AUTOSAR DiagnosticEventWindow."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_window", None, False, False, DiagnosticEventWindow),  # eventWindow
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventWindow."""
        super().__init__()
        self.event_window: Optional[DiagnosticEventWindow] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventWindow to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventWindow":
        """Create DiagnosticEventWindow from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventWindow instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventWindow since parent returns ARObject
        return cast("DiagnosticEventWindow", obj)


class DiagnosticEventWindowBuilder:
    """Builder for DiagnosticEventWindow."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventWindow = DiagnosticEventWindow()

    def build(self) -> DiagnosticEventWindow:
        """Build and return DiagnosticEventWindow object.

        Returns:
            DiagnosticEventWindow instance
        """
        # TODO: Add validation
        return self._obj
