"""DiagnosticReadDataByPeriodicID AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDataByPeriodicID."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_data_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicID."""
        super().__init__()
        self.read_data_class: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicID":
        """Deserialize XML element to DiagnosticReadDataByPeriodicID object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByPeriodicID object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByPeriodicID, cls).deserialize(element)

        # Parse read_data_class
        child = ARObject._find_child_element(element, "READ-DATA-CLASS")
        if child is not None:
            read_data_class_value = child.text
            obj.read_data_class = read_data_class_value

        return obj



class DiagnosticReadDataByPeriodicIDBuilder:
    """Builder for DiagnosticReadDataByPeriodicID."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicID = DiagnosticReadDataByPeriodicID()

    def build(self) -> DiagnosticReadDataByPeriodicID:
        """Build and return DiagnosticReadDataByPeriodicID object.

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # TODO: Add validation
        return self._obj
