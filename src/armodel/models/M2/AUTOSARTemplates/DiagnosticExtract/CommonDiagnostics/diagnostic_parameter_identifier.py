"""DiagnosticParameterIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)


class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticParameterIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_elements", None, False, True, DiagnosticParameter),  # dataElements
        ("id", None, True, False, None),  # id
        ("pid_size", None, True, False, None),  # pidSize
        ("support_info_byte", None, False, False, DiagnosticSupportInfoByte),  # supportInfoByte
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
        self.pid_size: Optional[PositiveInteger] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticParameterIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdentifier":
        """Create DiagnosticParameterIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticParameterIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticParameterIdentifier since parent returns ARObject
        return cast("DiagnosticParameterIdentifier", obj)


class DiagnosticParameterIdentifierBuilder:
    """Builder for DiagnosticParameterIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdentifier = DiagnosticParameterIdentifier()

    def build(self) -> DiagnosticParameterIdentifier:
        """Build and return DiagnosticParameterIdentifier object.

        Returns:
            DiagnosticParameterIdentifier instance
        """
        # TODO: Add validation
        return self._obj
