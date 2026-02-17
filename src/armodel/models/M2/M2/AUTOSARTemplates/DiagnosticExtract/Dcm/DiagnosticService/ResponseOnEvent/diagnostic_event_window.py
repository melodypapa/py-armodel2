"""DiagnosticEventWindow AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEventWindow(ARObject):
    """AUTOSAR DiagnosticEventWindow."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_window": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="DiagnosticEventWindow",
        ),  # eventWindow
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventWindow."""
        super().__init__()
        self.event_window: Optional[DiagnosticEventWindow] = None


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
