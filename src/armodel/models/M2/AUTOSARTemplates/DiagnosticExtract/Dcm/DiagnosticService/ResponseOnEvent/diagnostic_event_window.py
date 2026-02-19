"""DiagnosticEventWindow AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEventWindow(ARObject):
    """AUTOSAR DiagnosticEventWindow."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_window: Optional[DiagnosticEventWindow]
    def __init__(self) -> None:
        """Initialize DiagnosticEventWindow."""
        super().__init__()
        self.event_window: Optional[DiagnosticEventWindow] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventWindow":
        """Deserialize XML element to DiagnosticEventWindow object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventWindow object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_window
        child = ARObject._find_child_element(element, "EVENT-WINDOW")
        if child is not None:
            event_window_value = ARObject._deserialize_by_tag(child, "DiagnosticEventWindow")
            obj.event_window = event_window_value

        return obj



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
