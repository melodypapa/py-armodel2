"""DiagnosticDataIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """AUTOSAR DiagnosticDataIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifiers: list[DiagnosticDataIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifierSet."""
        super().__init__()
        self.data_identifiers: list[DiagnosticDataIdentifier] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataIdentifierSet":
        """Deserialize XML element to DiagnosticDataIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataIdentifierSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_identifiers (list)
        obj.data_identifiers = []
        for child in ARObject._find_all_child_elements(element, "DATA-IDENTIFIERS"):
            data_identifiers_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.data_identifiers.append(data_identifiers_value)

        return obj



class DiagnosticDataIdentifierSetBuilder:
    """Builder for DiagnosticDataIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataIdentifierSet = DiagnosticDataIdentifierSet()

    def build(self) -> DiagnosticDataIdentifierSet:
        """Build and return DiagnosticDataIdentifierSet object.

        Returns:
            DiagnosticDataIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
