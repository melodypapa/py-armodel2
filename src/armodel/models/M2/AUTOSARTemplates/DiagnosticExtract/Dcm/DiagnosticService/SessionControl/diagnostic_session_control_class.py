"""DiagnosticSessionControlClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticSessionControlClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("s3_server", None, True, False, None),  # s3Server
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSessionControlClass."""
        super().__init__()
        self.s3_server: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSessionControlClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControlClass":
        """Create DiagnosticSessionControlClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSessionControlClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSessionControlClass since parent returns ARObject
        return cast("DiagnosticSessionControlClass", obj)


class DiagnosticSessionControlClassBuilder:
    """Builder for DiagnosticSessionControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControlClass = DiagnosticSessionControlClass()

    def build(self) -> DiagnosticSessionControlClass:
        """Build and return DiagnosticSessionControlClass object.

        Returns:
            DiagnosticSessionControlClass instance
        """
        # TODO: Add validation
        return self._obj
