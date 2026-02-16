"""DiagnosticAbstractDataIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAbstractDataIdentifier."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAbstractDataIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAbstractDataIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAbstractDataIdentifier":
        """Create DiagnosticAbstractDataIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAbstractDataIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAbstractDataIdentifier since parent returns ARObject
        return cast("DiagnosticAbstractDataIdentifier", obj)


class DiagnosticAbstractDataIdentifierBuilder:
    """Builder for DiagnosticAbstractDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractDataIdentifier = DiagnosticAbstractDataIdentifier()

    def build(self) -> DiagnosticAbstractDataIdentifier:
        """Build and return DiagnosticAbstractDataIdentifier object.

        Returns:
            DiagnosticAbstractDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
