"""DiagnosticEcuResetClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset import (
    DiagnosticResponseToEcuResetEnum,
)


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticEcuResetClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    respond_to: Optional[DiagnosticResponseToEcuResetEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuResetClass."""
        super().__init__()
        self.respond_to: Optional[DiagnosticResponseToEcuResetEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuResetClass":
        """Deserialize XML element to DiagnosticEcuResetClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuResetClass object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse respond_to
        child = ARObject._find_child_element(element, "RESPOND-TO")
        if child is not None:
            respond_to_value = child.text
            obj.respond_to = respond_to_value

        return obj



class DiagnosticEcuResetClassBuilder:
    """Builder for DiagnosticEcuResetClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuResetClass = DiagnosticEcuResetClass()

    def build(self) -> DiagnosticEcuResetClass:
        """Build and return DiagnosticEcuResetClass object.

        Returns:
            DiagnosticEcuResetClass instance
        """
        # TODO: Add validation
        return self._obj
