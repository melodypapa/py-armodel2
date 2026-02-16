"""DiagnosticJ1939Spn AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Spn."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("spn", None, True, False, None),  # spn
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Spn."""
        super().__init__()
        self.spn: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticJ1939Spn to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Spn":
        """Create DiagnosticJ1939Spn from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticJ1939Spn instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticJ1939Spn since parent returns ARObject
        return cast("DiagnosticJ1939Spn", obj)


class DiagnosticJ1939SpnBuilder:
    """Builder for DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Spn = DiagnosticJ1939Spn()

    def build(self) -> DiagnosticJ1939Spn:
        """Build and return DiagnosticJ1939Spn object.

        Returns:
            DiagnosticJ1939Spn instance
        """
        # TODO: Add validation
        return self._obj
