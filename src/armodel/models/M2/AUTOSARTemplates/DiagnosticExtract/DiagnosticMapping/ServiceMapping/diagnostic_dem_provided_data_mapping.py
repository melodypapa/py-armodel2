"""DiagnosticDemProvidedDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticDemProvidedDataMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticDataElement,
        ),  # dataElement
        "data_provider": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataProvider
    }

    def __init__(self) -> None:
        """Initialize DiagnosticDemProvidedDataMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.data_provider: Optional[NameToken] = None


class DiagnosticDemProvidedDataMappingBuilder:
    """Builder for DiagnosticDemProvidedDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDemProvidedDataMapping = DiagnosticDemProvidedDataMapping()

    def build(self) -> DiagnosticDemProvidedDataMapping:
        """Build and return DiagnosticDemProvidedDataMapping object.

        Returns:
            DiagnosticDemProvidedDataMapping instance
        """
        # TODO: Add validation
        return self._obj
