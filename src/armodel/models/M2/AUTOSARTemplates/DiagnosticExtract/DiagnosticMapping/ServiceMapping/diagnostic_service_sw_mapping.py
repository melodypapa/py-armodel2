"""DiagnosticServiceSwMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceSwMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accessed_data", None, False, False, DataPrototype),  # accessedData
        ("diagnostic_data", None, False, False, DiagnosticDataElement),  # diagnosticData
        ("diagnostic", None, False, False, DiagnosticParameter),  # diagnostic
        ("mapped_bsw", None, False, False, any (BswService)),  # mappedBsw
        ("mapped_flat_swc", None, False, False, any (SwcService)),  # mappedFlatSwc
        ("mapped_swc", None, False, False, any (SwcService)),  # mappedSwc
        ("parameter", None, False, False, DiagnosticParameter),  # parameter
        ("service_instance", None, False, False, any (DiagnosticService)),  # serviceInstance
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticServiceSwMapping."""
        super().__init__()
        self.accessed_data: Optional[DataPrototype] = None
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
        self.diagnostic: Optional[DiagnosticParameter] = None
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None
        self.parameter: Optional[DiagnosticParameter] = None
        self.service_instance: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticServiceSwMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceSwMapping":
        """Create DiagnosticServiceSwMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticServiceSwMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticServiceSwMapping since parent returns ARObject
        return cast("DiagnosticServiceSwMapping", obj)


class DiagnosticServiceSwMappingBuilder:
    """Builder for DiagnosticServiceSwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceSwMapping = DiagnosticServiceSwMapping()

    def build(self) -> DiagnosticServiceSwMapping:
        """Build and return DiagnosticServiceSwMapping object.

        Returns:
            DiagnosticServiceSwMapping instance
        """
        # TODO: Add validation
        return self._obj
