"""DiagnosticIoControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticIoControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticIoControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticIoControlClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIoControlClass":
        """Deserialize XML element to DiagnosticIoControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIoControlClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticIoControlClass, cls).deserialize(element)



class DiagnosticIoControlClassBuilder:
    """Builder for DiagnosticIoControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlClass = DiagnosticIoControlClass()

    def build(self) -> DiagnosticIoControlClass:
        """Build and return DiagnosticIoControlClass object.

        Returns:
            DiagnosticIoControlClass instance
        """
        # TODO: Add validation
        return self._obj
