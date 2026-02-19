"""DiagnosticAuthentication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 98)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticAuthentication(DiagnosticServiceInstance, ABC):
    """AUTOSAR DiagnosticAuthentication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    authentication: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthentication."""
        super().__init__()
        self.authentication: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthentication":
        """Deserialize XML element to DiagnosticAuthentication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthentication object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthentication, cls).deserialize(element)

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = child.text
            obj.authentication = authentication_value

        return obj



class DiagnosticAuthenticationBuilder:
    """Builder for DiagnosticAuthentication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthentication = DiagnosticAuthentication()

    def build(self) -> DiagnosticAuthentication:
        """Build and return DiagnosticAuthentication object.

        Returns:
            DiagnosticAuthentication instance
        """
        # TODO: Add validation
        return self._obj
