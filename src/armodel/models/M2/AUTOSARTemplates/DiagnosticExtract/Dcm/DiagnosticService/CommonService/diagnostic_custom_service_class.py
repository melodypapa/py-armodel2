"""DiagnosticCustomServiceClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticCustomServiceClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_service", None, True, False, None),  # customService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceClass."""
        super().__init__()
        self.custom_service: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticCustomServiceClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCustomServiceClass":
        """Create DiagnosticCustomServiceClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticCustomServiceClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticCustomServiceClass since parent returns ARObject
        return cast("DiagnosticCustomServiceClass", obj)


class DiagnosticCustomServiceClassBuilder:
    """Builder for DiagnosticCustomServiceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceClass = DiagnosticCustomServiceClass()

    def build(self) -> DiagnosticCustomServiceClass:
        """Build and return DiagnosticCustomServiceClass object.

        Returns:
            DiagnosticCustomServiceClass instance
        """
        # TODO: Add validation
        return self._obj
