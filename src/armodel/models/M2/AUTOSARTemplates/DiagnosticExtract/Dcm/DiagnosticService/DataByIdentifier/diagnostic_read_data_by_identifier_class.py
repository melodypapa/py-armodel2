"""DiagnosticReadDataByIdentifierClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByIdentifierClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_did_to_read", None, True, False, None),  # maxDidToRead
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifierClass."""
        super().__init__()
        self.max_did_to_read: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadDataByIdentifierClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByIdentifierClass":
        """Create DiagnosticReadDataByIdentifierClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadDataByIdentifierClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadDataByIdentifierClass since parent returns ARObject
        return cast("DiagnosticReadDataByIdentifierClass", obj)


class DiagnosticReadDataByIdentifierClassBuilder:
    """Builder for DiagnosticReadDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifierClass = DiagnosticReadDataByIdentifierClass()

    def build(self) -> DiagnosticReadDataByIdentifierClass:
        """Build and return DiagnosticReadDataByIdentifierClass object.

        Returns:
            DiagnosticReadDataByIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
