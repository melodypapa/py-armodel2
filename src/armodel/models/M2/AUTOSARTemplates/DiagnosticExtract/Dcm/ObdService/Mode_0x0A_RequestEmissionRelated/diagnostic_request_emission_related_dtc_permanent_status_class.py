"""DiagnosticRequestEmissionRelatedDTCPermanentStatusClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x0A_RequestEmissionRelated.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestEmissionRelatedDTCPermanentStatusClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCPermanentStatusClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCPermanentStatusClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass":
        """Deserialize XML element to DiagnosticRequestEmissionRelatedDTCPermanentStatusClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestEmissionRelatedDTCPermanentStatusClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestEmissionRelatedDTCPermanentStatusClass, cls).deserialize(element)



class DiagnosticRequestEmissionRelatedDTCPermanentStatusClassBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCPermanentStatusClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCPermanentStatusClass = DiagnosticRequestEmissionRelatedDTCPermanentStatusClass()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatusClass:
        """Build and return DiagnosticRequestEmissionRelatedDTCPermanentStatusClass object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatusClass instance
        """
        # TODO: Add validation
        return self._obj
