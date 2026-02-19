"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 127)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifier: Optional[DiagnosticDynamicDataIdentifier]
    dynamically: Optional[Any]
    max_source: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticDynamicDataIdentifier] = None
        self.dynamically: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_identifier
        child = ARObject._find_child_element(element, "DATA-IDENTIFIER")
        if child is not None:
            data_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticDynamicDataIdentifier")
            obj.data_identifier = data_identifier_value

        # Parse dynamically
        child = ARObject._find_child_element(element, "DYNAMICALLY")
        if child is not None:
            dynamically_value = child.text
            obj.dynamically = dynamically_value

        # Parse max_source
        child = ARObject._find_child_element(element, "MAX-SOURCE")
        if child is not None:
            max_source_value = child.text
            obj.max_source = max_source_value

        return obj



class DiagnosticDynamicallyDefineDataIdentifierBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return DiagnosticDynamicallyDefineDataIdentifier object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
