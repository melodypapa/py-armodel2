"""DiagnosticRequestCurrentPowertrainDataClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 151)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x01_RequestCurrentPowertrain.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestCurrentPowertrainDataClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestCurrentPowertrainDataClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainDataClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestCurrentPowertrainDataClass":
        """Deserialize XML element to DiagnosticRequestCurrentPowertrainDataClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestCurrentPowertrainDataClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestCurrentPowertrainDataClass, cls).deserialize(element)



class DiagnosticRequestCurrentPowertrainDataClassBuilder:
    """Builder for DiagnosticRequestCurrentPowertrainDataClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestCurrentPowertrainDataClass = DiagnosticRequestCurrentPowertrainDataClass()

    def build(self) -> DiagnosticRequestCurrentPowertrainDataClass:
        """Build and return DiagnosticRequestCurrentPowertrainDataClass object.

        Returns:
            DiagnosticRequestCurrentPowertrainDataClass instance
        """
        # TODO: Add validation
        return self._obj
