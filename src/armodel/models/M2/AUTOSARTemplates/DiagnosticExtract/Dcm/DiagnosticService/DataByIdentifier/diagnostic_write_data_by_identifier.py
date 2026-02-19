"""DiagnosticWriteDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticWriteDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticWriteDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    write_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticWriteDataByIdentifier."""
        super().__init__()
        self.write_class: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteDataByIdentifier":
        """Deserialize XML element to DiagnosticWriteDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticWriteDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticWriteDataByIdentifier, cls).deserialize(element)

        # Parse write_class
        child = ARObject._find_child_element(element, "WRITE-CLASS")
        if child is not None:
            write_class_value = child.text
            obj.write_class = write_class_value

        return obj



class DiagnosticWriteDataByIdentifierBuilder:
    """Builder for DiagnosticWriteDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteDataByIdentifier = DiagnosticWriteDataByIdentifier()

    def build(self) -> DiagnosticWriteDataByIdentifier:
        """Build and return DiagnosticWriteDataByIdentifier object.

        Returns:
            DiagnosticWriteDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
