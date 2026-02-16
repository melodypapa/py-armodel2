"""DiagnosticTestRoutineIdentifier AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestRoutineIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # id
        "request_data": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # requestData
        "response_data": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # responseData
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTestRoutineIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_data: Optional[PositiveInteger] = None
        self.response_data: Optional[PositiveInteger] = None


class DiagnosticTestRoutineIdentifierBuilder:
    """Builder for DiagnosticTestRoutineIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestRoutineIdentifier = DiagnosticTestRoutineIdentifier()

    def build(self) -> DiagnosticTestRoutineIdentifier:
        """Build and return DiagnosticTestRoutineIdentifier object.

        Returns:
            DiagnosticTestRoutineIdentifier instance
        """
        # TODO: Add validation
        return self._obj
