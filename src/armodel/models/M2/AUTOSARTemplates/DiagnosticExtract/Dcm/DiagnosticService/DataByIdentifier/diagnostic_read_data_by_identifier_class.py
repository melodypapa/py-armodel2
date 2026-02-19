"""DiagnosticReadDataByIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_did_to_read: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifierClass."""
        super().__init__()
        self.max_did_to_read: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByIdentifierClass":
        """Deserialize XML element to DiagnosticReadDataByIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByIdentifierClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByIdentifierClass, cls).deserialize(element)

        # Parse max_did_to_read
        child = ARObject._find_child_element(element, "MAX-DID-TO-READ")
        if child is not None:
            max_did_to_read_value = child.text
            obj.max_did_to_read = max_did_to_read_value

        return obj



class DiagnosticReadDataByIdentifierClassBuilder:
    """Builder for DiagnosticReadDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifierClass = DiagnosticReadDataByIdentifierClass()

    def build(self) -> DiagnosticReadDataByIdentifierClass:
        """Build and return DiagnosticReadDataByIdentifierClass object.

        Returns:
            DiagnosticReadDataByIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
