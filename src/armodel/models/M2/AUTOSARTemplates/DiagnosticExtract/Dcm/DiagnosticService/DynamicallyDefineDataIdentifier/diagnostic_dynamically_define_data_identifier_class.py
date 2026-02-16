"""DiagnosticDynamicallyDefineDataIdentifierClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("check_per", None, True, False, None),  # checkPer
        ("configuration", None, False, False, DiagnosticHandleDDDIConfigurationEnum),  # configuration
        ("subfunctions", None, False, True, any (DiagnosticDynamically)),  # subfunctions
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifierClass."""
        super().__init__()
        self.check_per: Optional[Boolean] = None
        self.configuration: Optional[DiagnosticHandleDDDIConfigurationEnum] = None
        self.subfunctions: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDynamicallyDefineDataIdentifierClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """Create DiagnosticDynamicallyDefineDataIdentifierClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDynamicallyDefineDataIdentifierClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDynamicallyDefineDataIdentifierClass since parent returns ARObject
        return cast("DiagnosticDynamicallyDefineDataIdentifierClass", obj)


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
