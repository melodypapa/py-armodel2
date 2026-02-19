"""DiagnosticSecurityLevel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSecurityLevel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_data: Optional[PositiveInteger]
    key_size: Optional[PositiveInteger]
    num_failed: Optional[PositiveInteger]
    security_delay: Optional[TimeValue]
    seed_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityLevel."""
        super().__init__()
        self.access_data: Optional[PositiveInteger] = None
        self.key_size: Optional[PositiveInteger] = None
        self.num_failed: Optional[PositiveInteger] = None
        self.security_delay: Optional[TimeValue] = None
        self.seed_size: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityLevel":
        """Deserialize XML element to DiagnosticSecurityLevel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityLevel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecurityLevel, cls).deserialize(element)

        # Parse access_data
        child = ARObject._find_child_element(element, "ACCESS-DATA")
        if child is not None:
            access_data_value = child.text
            obj.access_data = access_data_value

        # Parse key_size
        child = ARObject._find_child_element(element, "KEY-SIZE")
        if child is not None:
            key_size_value = child.text
            obj.key_size = key_size_value

        # Parse num_failed
        child = ARObject._find_child_element(element, "NUM-FAILED")
        if child is not None:
            num_failed_value = child.text
            obj.num_failed = num_failed_value

        # Parse security_delay
        child = ARObject._find_child_element(element, "SECURITY-DELAY")
        if child is not None:
            security_delay_value = child.text
            obj.security_delay = security_delay_value

        # Parse seed_size
        child = ARObject._find_child_element(element, "SEED-SIZE")
        if child is not None:
            seed_size_value = child.text
            obj.seed_size = seed_size_value

        return obj



class DiagnosticSecurityLevelBuilder:
    """Builder for DiagnosticSecurityLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityLevel = DiagnosticSecurityLevel()

    def build(self) -> DiagnosticSecurityLevel:
        """Build and return DiagnosticSecurityLevel object.

        Returns:
            DiagnosticSecurityLevel instance
        """
        # TODO: Add validation
        return self._obj
