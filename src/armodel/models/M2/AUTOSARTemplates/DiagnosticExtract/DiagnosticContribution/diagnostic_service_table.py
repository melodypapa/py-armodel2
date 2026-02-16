"""DiagnosticServiceTable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostics", None, False, True, DiagnosticConnection),  # diagnostics
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("protocol_kind", None, True, False, None),  # protocolKind
        ("service_instances", None, False, True, any (DiagnosticService)),  # serviceInstances
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticServiceTable."""
        super().__init__()
        self.diagnostics: list[DiagnosticConnection] = []
        self.ecu_instance: Optional[EcuInstance] = None
        self.protocol_kind: Optional[NameToken] = None
        self.service_instances: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticServiceTable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceTable":
        """Create DiagnosticServiceTable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticServiceTable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticServiceTable since parent returns ARObject
        return cast("DiagnosticServiceTable", obj)


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
