"""DiagnosticAuthRole AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticAuthRole(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAuthRole."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bit_position", None, True, False, None),  # bitPosition
        ("is_default", None, True, False, None),  # isDefault
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthRole."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None
        self.is_default: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthRole to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRole":
        """Create DiagnosticAuthRole from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthRole instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthRole since parent returns ARObject
        return cast("DiagnosticAuthRole", obj)


class DiagnosticAuthRoleBuilder:
    """Builder for DiagnosticAuthRole."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRole = DiagnosticAuthRole()

    def build(self) -> DiagnosticAuthRole:
        """Build and return DiagnosticAuthRole object.

        Returns:
            DiagnosticAuthRole instance
        """
        # TODO: Add validation
        return self._obj
