"""DiagnosticInfoType AUTOSAR element."""

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


class DiagnosticInfoType(DiagnosticCommonElement):
    """AUTOSAR DiagnosticInfoType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_elements", None, False, True, DiagnosticParameter),  # dataElements
        ("id", None, True, False, None),  # id
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticInfoType."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticInfoType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticInfoType":
        """Create DiagnosticInfoType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticInfoType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticInfoType since parent returns ARObject
        return cast("DiagnosticInfoType", obj)


class DiagnosticInfoTypeBuilder:
    """Builder for DiagnosticInfoType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInfoType = DiagnosticInfoType()

    def build(self) -> DiagnosticInfoType:
        """Build and return DiagnosticInfoType object.

        Returns:
            DiagnosticInfoType instance
        """
        # TODO: Add validation
        return self._obj
