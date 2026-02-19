"""DiagnosticServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from abc import ABC, abstractmethod


class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    access: Optional[DiagnosticAccessPermission]
    service_class: Optional[DiagnosticServiceClass]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceInstance."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.service_class: Optional[DiagnosticServiceClass] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceInstance":
        """Deserialize XML element to DiagnosticServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceInstance, cls).deserialize(element)

        # Parse access
        child = ARObject._find_child_element(element, "ACCESS")
        if child is not None:
            access_value = ARObject._deserialize_by_tag(child, "DiagnosticAccessPermission")
            obj.access = access_value

        # Parse service_class
        child = ARObject._find_child_element(element, "SERVICE-CLASS")
        if child is not None:
            service_class_value = ARObject._deserialize_by_tag(child, "DiagnosticServiceClass")
            obj.service_class = service_class_value

        return obj



class DiagnosticServiceInstanceBuilder:
    """Builder for DiagnosticServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceInstance = DiagnosticServiceInstance()

    def build(self) -> DiagnosticServiceInstance:
        """Build and return DiagnosticServiceInstance object.

        Returns:
            DiagnosticServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
