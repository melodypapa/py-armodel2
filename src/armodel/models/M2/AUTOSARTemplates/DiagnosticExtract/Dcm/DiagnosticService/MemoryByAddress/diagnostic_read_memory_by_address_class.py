"""DiagnosticReadMemoryByAddressClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadMemoryByAddressClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddressClass."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadMemoryByAddressClass":
        """Deserialize XML element to DiagnosticReadMemoryByAddressClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadMemoryByAddressClass object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class DiagnosticReadMemoryByAddressClassBuilder:
    """Builder for DiagnosticReadMemoryByAddressClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddressClass = DiagnosticReadMemoryByAddressClass()

    def build(self) -> DiagnosticReadMemoryByAddressClass:
        """Build and return DiagnosticReadMemoryByAddressClass object.

        Returns:
            DiagnosticReadMemoryByAddressClass instance
        """
        # TODO: Add validation
        return self._obj
