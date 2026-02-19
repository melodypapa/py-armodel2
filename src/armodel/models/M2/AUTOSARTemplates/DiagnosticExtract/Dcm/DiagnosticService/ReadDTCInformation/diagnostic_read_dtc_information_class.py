"""DiagnosticReadDTCInformationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadDTCInformationClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDTCInformationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformationClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDTCInformationClass":
        """Deserialize XML element to DiagnosticReadDTCInformationClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDTCInformationClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticReadDTCInformationClass, cls).deserialize(element)



class DiagnosticReadDTCInformationClassBuilder:
    """Builder for DiagnosticReadDTCInformationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformationClass = DiagnosticReadDTCInformationClass()

    def build(self) -> DiagnosticReadDTCInformationClass:
        """Build and return DiagnosticReadDTCInformationClass object.

        Returns:
            DiagnosticReadDTCInformationClass instance
        """
        # TODO: Add validation
        return self._obj
