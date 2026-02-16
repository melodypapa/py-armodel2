"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_identifier": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticDynamicDataIdentifier,
        ),  # dataIdentifier
        "dynamically": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticDynamically),
        ),  # dynamically
        "max_source": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSource
    }

    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticDynamicDataIdentifier] = None
        self.dynamically: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None


class DiagnosticDynamicallyDefineDataIdentifierBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return DiagnosticDynamicallyDefineDataIdentifier object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
