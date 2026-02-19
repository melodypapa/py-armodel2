"""DiagnosticStorageConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_storage: Optional[Any]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionPortMapping":
        """Deserialize XML element to DiagnosticStorageConditionPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionPortMapping, cls).deserialize(element)

        # Parse diagnostic_storage
        child = ARObject._find_child_element(element, "DIAGNOSTIC-STORAGE")
        if child is not None:
            diagnostic_storage_value = child.text
            obj.diagnostic_storage = diagnostic_storage_value

        # Parse swc_flat_service
        child = ARObject._find_child_element(element, "SWC-FLAT-SERVICE")
        if child is not None:
            swc_flat_service_value = child.text
            obj.swc_flat_service = swc_flat_service_value

        # Parse swc_service
        child = ARObject._find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticStorageConditionPortMappingBuilder:
    """Builder for DiagnosticStorageConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()

    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return DiagnosticStorageConditionPortMapping object.

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
