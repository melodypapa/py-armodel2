"""DiagnosticParameter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_parameter import (
    DiagnosticAbstractParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameter(DiagnosticAbstractParameter):
    """AUTOSAR DiagnosticParameter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ident", None, False, False, DiagnosticParameter),  # ident
        ("support_info", None, False, False, DiagnosticParameter),  # supportInfo
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticParameter."""
        super().__init__()
        self.ident: Optional[DiagnosticParameter] = None
        self.support_info: Optional[DiagnosticParameter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticParameter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameter":
        """Create DiagnosticParameter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticParameter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticParameter since parent returns ARObject
        return cast("DiagnosticParameter", obj)


class DiagnosticParameterBuilder:
    """Builder for DiagnosticParameter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameter = DiagnosticParameter()

    def build(self) -> DiagnosticParameter:
        """Build and return DiagnosticParameter object.

        Returns:
            DiagnosticParameter instance
        """
        # TODO: Add validation
        return self._obj
