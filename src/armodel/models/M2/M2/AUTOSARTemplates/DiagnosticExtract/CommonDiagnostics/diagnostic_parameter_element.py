"""DiagnosticParameterElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElement(Identifiable):
    """AUTOSAR DiagnosticParameterElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # arraySize
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # subElements
    }

    def __init__(self) -> None:
        """Initialize DiagnosticParameterElement."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.sub_elements: list[DiagnosticParameter] = []


class DiagnosticParameterElementBuilder:
    """Builder for DiagnosticParameterElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElement = DiagnosticParameterElement()

    def build(self) -> DiagnosticParameterElement:
        """Build and return DiagnosticParameterElement object.

        Returns:
            DiagnosticParameterElement instance
        """
        # TODO: Add validation
        return self._obj
