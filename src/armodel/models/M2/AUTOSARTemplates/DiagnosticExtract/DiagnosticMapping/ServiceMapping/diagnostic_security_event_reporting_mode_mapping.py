"""DiagnosticSecurityEventReportingModeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 243)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecurityEventReportingModeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element: Optional[DiagnosticDataElement]
    security_event_context: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityEventReportingModeMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.security_event_context: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityEventReportingModeMapping":
        """Deserialize XML element to DiagnosticSecurityEventReportingModeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityEventReportingModeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_value = ARObject._deserialize_by_tag(child, "DiagnosticDataElement")
            obj.data_element = data_element_value

        # Parse security_event_context
        child = ARObject._find_child_element(element, "SECURITY-EVENT-CONTEXT")
        if child is not None:
            security_event_context_value = child.text
            obj.security_event_context = security_event_context_value

        return obj



class DiagnosticSecurityEventReportingModeMappingBuilder:
    """Builder for DiagnosticSecurityEventReportingModeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityEventReportingModeMapping = DiagnosticSecurityEventReportingModeMapping()

    def build(self) -> DiagnosticSecurityEventReportingModeMapping:
        """Build and return DiagnosticSecurityEventReportingModeMapping object.

        Returns:
            DiagnosticSecurityEventReportingModeMapping instance
        """
        # TODO: Add validation
        return self._obj
