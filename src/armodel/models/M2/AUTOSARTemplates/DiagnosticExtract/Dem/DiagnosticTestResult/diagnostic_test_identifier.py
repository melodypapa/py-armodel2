"""DiagnosticTestIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestIdentifier(ARObject):
    """AUTOSAR DiagnosticTestIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
        ("uas_id", None, True, False, None),  # uasId
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTestIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.uas_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTestIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestIdentifier":
        """Create DiagnosticTestIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTestIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTestIdentifier since parent returns ARObject
        return cast("DiagnosticTestIdentifier", obj)


class DiagnosticTestIdentifierBuilder:
    """Builder for DiagnosticTestIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestIdentifier = DiagnosticTestIdentifier()

    def build(self) -> DiagnosticTestIdentifier:
        """Build and return DiagnosticTestIdentifier object.

        Returns:
            DiagnosticTestIdentifier instance
        """
        # TODO: Add validation
        return self._obj
