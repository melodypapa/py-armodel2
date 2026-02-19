"""DiagnosticCustomServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CustomServiceInstance.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticCustomServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceInstance."""
        super().__init__()
        self.custom_service: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCustomServiceInstance":
        """Deserialize XML element to DiagnosticCustomServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCustomServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCustomServiceInstance, cls).deserialize(element)

        # Parse custom_service
        child = ARObject._find_child_element(element, "CUSTOM-SERVICE")
        if child is not None:
            custom_service_value = child.text
            obj.custom_service = custom_service_value

        return obj



class DiagnosticCustomServiceInstanceBuilder:
    """Builder for DiagnosticCustomServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceInstance = DiagnosticCustomServiceInstance()

    def build(self) -> DiagnosticCustomServiceInstance:
        """Build and return DiagnosticCustomServiceInstance object.

        Returns:
            DiagnosticCustomServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
