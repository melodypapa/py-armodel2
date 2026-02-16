"""DiagnosticIumprToFunctionIdentifierMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticIumprToFunctionIdentifierMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("function", None, False, False, any (DiagnosticFunction)),  # function
        ("iumpr", None, False, False, DiagnosticIumpr),  # iumpr
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIumprToFunctionIdentifierMapping."""
        super().__init__()
        self.function: Optional[Any] = None
        self.iumpr: Optional[DiagnosticIumpr] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIumprToFunctionIdentifierMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprToFunctionIdentifierMapping":
        """Create DiagnosticIumprToFunctionIdentifierMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIumprToFunctionIdentifierMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIumprToFunctionIdentifierMapping since parent returns ARObject
        return cast("DiagnosticIumprToFunctionIdentifierMapping", obj)


class DiagnosticIumprToFunctionIdentifierMappingBuilder:
    """Builder for DiagnosticIumprToFunctionIdentifierMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprToFunctionIdentifierMapping = DiagnosticIumprToFunctionIdentifierMapping()

    def build(self) -> DiagnosticIumprToFunctionIdentifierMapping:
        """Build and return DiagnosticIumprToFunctionIdentifierMapping object.

        Returns:
            DiagnosticIumprToFunctionIdentifierMapping instance
        """
        # TODO: Add validation
        return self._obj
