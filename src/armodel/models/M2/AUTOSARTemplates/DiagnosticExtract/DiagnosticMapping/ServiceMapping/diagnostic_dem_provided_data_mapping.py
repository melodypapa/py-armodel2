"""DiagnosticDemProvidedDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticDemProvidedDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element: Optional[DiagnosticDataElement]
    data_provider: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DiagnosticDemProvidedDataMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.data_provider: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDemProvidedDataMapping":
        """Deserialize XML element to DiagnosticDemProvidedDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDemProvidedDataMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_value = ARObject._deserialize_by_tag(child, "DiagnosticDataElement")
            obj.data_element = data_element_value

        # Parse data_provider
        child = ARObject._find_child_element(element, "DATA-PROVIDER")
        if child is not None:
            data_provider_value = child.text
            obj.data_provider = data_provider_value

        return obj



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
