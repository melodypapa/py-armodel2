"""DiagnosticSecureCodingMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 312)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)


class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecureCodingMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifiers: list[Any]
    validation: Optional[DiagnosticStartRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticSecureCodingMapping."""
        super().__init__()
        self.data_identifiers: list[Any] = []
        self.validation: Optional[DiagnosticStartRoutine] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecureCodingMapping":
        """Deserialize XML element to DiagnosticSecureCodingMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecureCodingMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_identifiers (list)
        obj.data_identifiers = []
        for child in ARObject._find_all_child_elements(element, "DATA-IDENTIFIERS"):
            data_identifiers_value = child.text
            obj.data_identifiers.append(data_identifiers_value)

        # Parse validation
        child = ARObject._find_child_element(element, "VALIDATION")
        if child is not None:
            validation_value = ARObject._deserialize_by_tag(child, "DiagnosticStartRoutine")
            obj.validation = validation_value

        return obj



class DiagnosticSecureCodingMappingBuilder:
    """Builder for DiagnosticSecureCodingMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecureCodingMapping = DiagnosticSecureCodingMapping()

    def build(self) -> DiagnosticSecureCodingMapping:
        """Build and return DiagnosticSecureCodingMapping object.

        Returns:
            DiagnosticSecureCodingMapping instance
        """
        # TODO: Add validation
        return self._obj
