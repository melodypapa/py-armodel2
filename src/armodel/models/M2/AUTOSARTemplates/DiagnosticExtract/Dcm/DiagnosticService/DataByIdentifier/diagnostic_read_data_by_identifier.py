"""DiagnosticReadDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifier."""
        super().__init__()
        self.read_class: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByIdentifier":
        """Deserialize XML element to DiagnosticReadDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByIdentifier, cls).deserialize(element)

        # Parse read_class
        child = ARObject._find_child_element(element, "READ-CLASS")
        if child is not None:
            read_class_value = child.text
            obj.read_class = read_class_value

        return obj



class DiagnosticReadDataByIdentifierBuilder:
    """Builder for DiagnosticReadDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifier = DiagnosticReadDataByIdentifier()

    def build(self) -> DiagnosticReadDataByIdentifier:
        """Build and return DiagnosticReadDataByIdentifier object.

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
