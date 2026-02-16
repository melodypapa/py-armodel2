"""DiagnosticSession AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSession(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSession."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
        ("jump_to_boot", None, False, False, DiagnosticJumpToBootLoaderEnum),  # jumpToBoot
        ("p2_server_max", None, True, False, None),  # p2ServerMax
        ("p2_star_server", None, True, False, None),  # p2StarServer
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSession."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum] = None
        self.p2_server_max: Optional[TimeValue] = None
        self.p2_star_server: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSession to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSession":
        """Create DiagnosticSession from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSession instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSession since parent returns ARObject
        return cast("DiagnosticSession", obj)


class DiagnosticSessionBuilder:
    """Builder for DiagnosticSession."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSession = DiagnosticSession()

    def build(self) -> DiagnosticSession:
        """Build and return DiagnosticSession object.

        Returns:
            DiagnosticSession instance
        """
        # TODO: Add validation
        return self._obj
