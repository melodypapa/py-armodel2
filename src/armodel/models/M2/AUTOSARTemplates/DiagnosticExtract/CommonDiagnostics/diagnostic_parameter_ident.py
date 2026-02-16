"""DiagnosticParameterIdent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterIdent(IdentCaption):
    """AUTOSAR DiagnosticParameterIdent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # subElements
    }

    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdent."""
        super().__init__()
        self.sub_elements: list[DiagnosticParameter] = []


class DiagnosticParameterIdentBuilder:
    """Builder for DiagnosticParameterIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdent = DiagnosticParameterIdent()

    def build(self) -> DiagnosticParameterIdent:
        """Build and return DiagnosticParameterIdent object.

        Returns:
            DiagnosticParameterIdent instance
        """
        # TODO: Add validation
        return self._obj
