"""DiagnosticParameterElementAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElementAccess(ARObject):
    """AUTOSAR DiagnosticParameterElementAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # contextElements
        "target_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticParameter,
        ),  # targetElement
    }

    def __init__(self) -> None:
        """Initialize DiagnosticParameterElementAccess."""
        super().__init__()
        self.context_elements: list[DiagnosticParameter] = []
        self.target_element: Optional[DiagnosticParameter] = None


class DiagnosticParameterElementAccessBuilder:
    """Builder for DiagnosticParameterElementAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElementAccess = DiagnosticParameterElementAccess()

    def build(self) -> DiagnosticParameterElementAccess:
        """Build and return DiagnosticParameterElementAccess object.

        Returns:
            DiagnosticParameterElementAccess instance
        """
        # TODO: Add validation
        return self._obj
