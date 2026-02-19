"""DiagnosticServiceTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticServiceTable(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostics: list[DiagnosticConnection]
    ecu_instance: Optional[EcuInstance]
    protocol_kind: Optional[NameToken]
    service_instances: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceTable."""
        super().__init__()
        self.diagnostics: list[DiagnosticConnection] = []
        self.ecu_instance: Optional[EcuInstance] = None
        self.protocol_kind: Optional[NameToken] = None
        self.service_instances: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceTable":
        """Deserialize XML element to DiagnosticServiceTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceTable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse diagnostics (list)
        obj.diagnostics = []
        for child in ARObject._find_all_child_elements(element, "DIAGNOSTICS"):
            diagnostics_value = ARObject._deserialize_by_tag(child, "DiagnosticConnection")
            obj.diagnostics.append(diagnostics_value)

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse protocol_kind
        child = ARObject._find_child_element(element, "PROTOCOL-KIND")
        if child is not None:
            protocol_kind_value = child.text
            obj.protocol_kind = protocol_kind_value

        # Parse service_instances (list)
        obj.service_instances = []
        for child in ARObject._find_all_child_elements(element, "SERVICE-INSTANCES"):
            service_instances_value = child.text
            obj.service_instances.append(service_instances_value)

        return obj



class DiagnosticServiceTableBuilder:
    """Builder for DiagnosticServiceTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceTable = DiagnosticServiceTable()

    def build(self) -> DiagnosticServiceTable:
        """Build and return DiagnosticServiceTable object.

        Returns:
            DiagnosticServiceTable instance
        """
        # TODO: Add validation
        return self._obj
