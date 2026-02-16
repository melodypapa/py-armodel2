"""DiagnosticFunctionInhibitSource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DiagnosticFunctionInhibitSource(Identifiable):
    """AUTOSAR DiagnosticFunctionInhibitSource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event", None, False, False, any (DiagnosticFimAlias)),  # event
        ("event_group", None, False, False, any (DiagnosticFimAlias)),  # eventGroup
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFunctionInhibitSource."""
        super().__init__()
        self.event: Optional[Any] = None
        self.event_group: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFunctionInhibitSource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionInhibitSource":
        """Create DiagnosticFunctionInhibitSource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFunctionInhibitSource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFunctionInhibitSource since parent returns ARObject
        return cast("DiagnosticFunctionInhibitSource", obj)


class DiagnosticFunctionInhibitSourceBuilder:
    """Builder for DiagnosticFunctionInhibitSource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionInhibitSource = DiagnosticFunctionInhibitSource()

    def build(self) -> DiagnosticFunctionInhibitSource:
        """Build and return DiagnosticFunctionInhibitSource object.

        Returns:
            DiagnosticFunctionInhibitSource instance
        """
        # TODO: Add validation
        return self._obj
