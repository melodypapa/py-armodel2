"""DiagnosticSecurityAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SecurityAccess.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSecurityAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_seed_id: Optional[PositiveInteger]
    security_access: Optional[Any]
    security_delay: Optional[TimeValue]
    security_level: Optional[DiagnosticSecurityLevel]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityAccess."""
        super().__init__()
        self.request_seed_id: Optional[PositiveInteger] = None
        self.security_access: Optional[Any] = None
        self.security_delay: Optional[TimeValue] = None
        self.security_level: Optional[DiagnosticSecurityLevel] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityAccess":
        """Deserialize XML element to DiagnosticSecurityAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityAccess object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse request_seed_id
        child = ARObject._find_child_element(element, "REQUEST-SEED-ID")
        if child is not None:
            request_seed_id_value = child.text
            obj.request_seed_id = request_seed_id_value

        # Parse security_access
        child = ARObject._find_child_element(element, "SECURITY-ACCESS")
        if child is not None:
            security_access_value = child.text
            obj.security_access = security_access_value

        # Parse security_delay
        child = ARObject._find_child_element(element, "SECURITY-DELAY")
        if child is not None:
            security_delay_value = child.text
            obj.security_delay = security_delay_value

        # Parse security_level
        child = ARObject._find_child_element(element, "SECURITY-LEVEL")
        if child is not None:
            security_level_value = ARObject._deserialize_by_tag(child, "DiagnosticSecurityLevel")
            obj.security_level = security_level_value

        return obj



class DiagnosticSecurityAccessBuilder:
    """Builder for DiagnosticSecurityAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityAccess = DiagnosticSecurityAccess()

    def build(self) -> DiagnosticSecurityAccess:
        """Build and return DiagnosticSecurityAccess object.

        Returns:
            DiagnosticSecurityAccess instance
        """
        # TODO: Add validation
        return self._obj
