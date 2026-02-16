"""DiagnosticTestRoutineIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestRoutineIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
        ("request_data", None, True, False, None),  # requestData
        ("response_data", None, True, False, None),  # responseData
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTestRoutineIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_data: Optional[PositiveInteger] = None
        self.response_data: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTestRoutineIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestRoutineIdentifier":
        """Create DiagnosticTestRoutineIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTestRoutineIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTestRoutineIdentifier since parent returns ARObject
        return cast("DiagnosticTestRoutineIdentifier", obj)


class DiagnosticTestRoutineIdentifierBuilder:
    """Builder for DiagnosticTestRoutineIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestRoutineIdentifier = DiagnosticTestRoutineIdentifier()

    def build(self) -> DiagnosticTestRoutineIdentifier:
        """Build and return DiagnosticTestRoutineIdentifier object.

        Returns:
            DiagnosticTestRoutineIdentifier instance
        """
        # TODO: Add validation
        return self._obj
