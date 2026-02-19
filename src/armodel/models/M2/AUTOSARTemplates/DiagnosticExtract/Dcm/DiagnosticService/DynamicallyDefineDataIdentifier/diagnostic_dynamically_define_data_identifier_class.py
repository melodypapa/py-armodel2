"""DiagnosticDynamicallyDefineDataIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineData import (
    DiagnosticHandleDDDIConfigurationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    check_per: Optional[Boolean]
    configuration: Optional[DiagnosticHandleDDDIConfigurationEnum]
    subfunctions: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifierClass."""
        super().__init__()
        self.check_per: Optional[Boolean] = None
        self.configuration: Optional[DiagnosticHandleDDDIConfigurationEnum] = None
        self.subfunctions: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifierClass object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse check_per
        child = ARObject._find_child_element(element, "CHECK-PER")
        if child is not None:
            check_per_value = child.text
            obj.check_per = check_per_value

        # Parse configuration
        child = ARObject._find_child_element(element, "CONFIGURATION")
        if child is not None:
            configuration_value = child.text
            obj.configuration = configuration_value

        # Parse subfunctions (list)
        obj.subfunctions = []
        for child in ARObject._find_all_child_elements(element, "SUBFUNCTIONS"):
            subfunctions_value = child.text
            obj.subfunctions.append(subfunctions_value)

        return obj



class DiagnosticDynamicallyDefineDataIdentifierClassBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifierClass = DiagnosticDynamicallyDefineDataIdentifierClass()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifierClass:
        """Build and return DiagnosticDynamicallyDefineDataIdentifierClass object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
