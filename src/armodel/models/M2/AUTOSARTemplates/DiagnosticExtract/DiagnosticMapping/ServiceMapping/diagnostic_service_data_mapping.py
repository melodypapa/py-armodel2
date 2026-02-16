"""DiagnosticServiceDataMapping AUTOSAR element."""

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


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceDataMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_data", None, False, False, DiagnosticDataElement),  # diagnosticData
        ("diagnostic", None, False, False, DiagnosticParameter),  # diagnostic
        ("mapped_data", None, False, False, DataPrototype),  # mappedData
        ("parameter", None, False, False, DiagnosticParameter),  # parameter
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticServiceDataMapping."""
        super().__init__()
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
        self.diagnostic: Optional[DiagnosticParameter] = None
        self.mapped_data: Optional[DataPrototype] = None
        self.parameter: Optional[DiagnosticParameter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticServiceDataMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceDataMapping":
        """Create DiagnosticServiceDataMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticServiceDataMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticServiceDataMapping since parent returns ARObject
        return cast("DiagnosticServiceDataMapping", obj)


class DiagnosticServiceDataMappingBuilder:
    """Builder for DiagnosticServiceDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceDataMapping = DiagnosticServiceDataMapping()

    def build(self) -> DiagnosticServiceDataMapping:
        """Build and return DiagnosticServiceDataMapping object.

        Returns:
            DiagnosticServiceDataMapping instance
        """
        # TODO: Add validation
        return self._obj
