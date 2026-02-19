"""DiagnosticReadScalingDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 116)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadScalingDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_scaling: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadScalingDataByIdentifier."""
        super().__init__()
        self.read_scaling: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadScalingDataByIdentifier":
        """Deserialize XML element to DiagnosticReadScalingDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadScalingDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadScalingDataByIdentifier, cls).deserialize(element)

        # Parse read_scaling
        child = ARObject._find_child_element(element, "READ-SCALING")
        if child is not None:
            read_scaling_value = child.text
            obj.read_scaling = read_scaling_value

        return obj



class DiagnosticReadScalingDataByIdentifierBuilder:
    """Builder for DiagnosticReadScalingDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadScalingDataByIdentifier = DiagnosticReadScalingDataByIdentifier()

    def build(self) -> DiagnosticReadScalingDataByIdentifier:
        """Build and return DiagnosticReadScalingDataByIdentifier object.

        Returns:
            DiagnosticReadScalingDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
