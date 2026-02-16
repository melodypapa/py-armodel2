"""DiagnosticParameterIdentifier AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)


class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticParameterIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # dataElements
        "id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # id
        "pid_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pidSize
        "support_info_byte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticSupportInfoByte,
        ),  # supportInfoByte
    }

    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
        self.pid_size: Optional[PositiveInteger] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None


class DiagnosticParameterIdentifierBuilder:
    """Builder for DiagnosticParameterIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdentifier = DiagnosticParameterIdentifier()

    def build(self) -> DiagnosticParameterIdentifier:
        """Build and return DiagnosticParameterIdentifier object.

        Returns:
            DiagnosticParameterIdentifier instance
        """
        # TODO: Add validation
        return self._obj
