"""SecurityEventDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventDefinition(IdsCommonElement):
    """AUTOSAR SecurityEventDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_symbol_name", None, False, False, any (SymbolPropsName)),  # eventSymbolName
        ("id", None, True, False, None),  # id
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventDefinition."""
        super().__init__()
        self.event_symbol_name: Optional[Any] = None
        self.id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventDefinition":
        """Create SecurityEventDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventDefinition since parent returns ARObject
        return cast("SecurityEventDefinition", obj)


class SecurityEventDefinitionBuilder:
    """Builder for SecurityEventDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventDefinition = SecurityEventDefinition()

    def build(self) -> SecurityEventDefinition:
        """Build and return SecurityEventDefinition object.

        Returns:
            SecurityEventDefinition instance
        """
        # TODO: Add validation
        return self._obj
