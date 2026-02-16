"""DiagnosticAbstractParameter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticAbstractParameter(ARObject):
    """AUTOSAR DiagnosticAbstractParameter."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bit_offset", None, True, False, None),  # bitOffset
        ("data_element", None, False, False, DiagnosticDataElement),  # dataElement
        ("parameter_size", None, True, False, None),  # parameterSize
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAbstractParameter."""
        super().__init__()
        self.bit_offset: Optional[PositiveInteger] = None
        self.data_element: Optional[DiagnosticDataElement] = None
        self.parameter_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAbstractParameter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAbstractParameter":
        """Create DiagnosticAbstractParameter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAbstractParameter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAbstractParameter since parent returns ARObject
        return cast("DiagnosticAbstractParameter", obj)


class DiagnosticAbstractParameterBuilder:
    """Builder for DiagnosticAbstractParameter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractParameter = DiagnosticAbstractParameter()

    def build(self) -> DiagnosticAbstractParameter:
        """Build and return DiagnosticAbstractParameter object.

        Returns:
            DiagnosticAbstractParameter instance
        """
        # TODO: Add validation
        return self._obj
