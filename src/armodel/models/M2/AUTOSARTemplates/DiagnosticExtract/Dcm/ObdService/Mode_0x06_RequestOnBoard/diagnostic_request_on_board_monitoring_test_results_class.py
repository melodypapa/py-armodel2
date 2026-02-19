"""DiagnosticRequestOnBoardMonitoringTestResultsClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x06_RequestOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestOnBoardMonitoringTestResultsClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestOnBoardMonitoringTestResultsClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestOnBoardMonitoringTestResultsClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestOnBoardMonitoringTestResultsClass":
        """Deserialize XML element to DiagnosticRequestOnBoardMonitoringTestResultsClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestOnBoardMonitoringTestResultsClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestOnBoardMonitoringTestResultsClass, cls).deserialize(element)



class DiagnosticRequestOnBoardMonitoringTestResultsClassBuilder:
    """Builder for DiagnosticRequestOnBoardMonitoringTestResultsClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestOnBoardMonitoringTestResultsClass = DiagnosticRequestOnBoardMonitoringTestResultsClass()

    def build(self) -> DiagnosticRequestOnBoardMonitoringTestResultsClass:
        """Build and return DiagnosticRequestOnBoardMonitoringTestResultsClass object.

        Returns:
            DiagnosticRequestOnBoardMonitoringTestResultsClass instance
        """
        # TODO: Add validation
        return self._obj
