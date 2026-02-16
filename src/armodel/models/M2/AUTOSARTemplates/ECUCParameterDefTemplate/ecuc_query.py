"""EcucQuery AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query_expression import (
    EcucQueryExpression,
)


class EcucQuery(Identifiable):
    """AUTOSAR EcucQuery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_query", None, False, False, EcucQueryExpression),  # ecucQuery
    ]

    def __init__(self) -> None:
        """Initialize EcucQuery."""
        super().__init__()
        self.ecuc_query: Optional[EcucQueryExpression] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucQuery to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucQuery":
        """Create EcucQuery from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucQuery instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucQuery since parent returns ARObject
        return cast("EcucQuery", obj)


class EcucQueryBuilder:
    """Builder for EcucQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucQuery = EcucQuery()

    def build(self) -> EcucQuery:
        """Build and return EcucQuery object.

        Returns:
            EcucQuery instance
        """
        # TODO: Add validation
        return self._obj
