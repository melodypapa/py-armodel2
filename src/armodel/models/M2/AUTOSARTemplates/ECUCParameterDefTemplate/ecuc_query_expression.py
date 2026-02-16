"""EcucQueryExpression AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)


class EcucQueryExpression(ARObject):
    """AUTOSAR EcucQueryExpression."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("config_element", None, False, False, EcucDefinitionElement),  # configElement
    ]

    def __init__(self) -> None:
        """Initialize EcucQueryExpression."""
        super().__init__()
        self.config_element: Optional[EcucDefinitionElement] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucQueryExpression to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucQueryExpression":
        """Create EcucQueryExpression from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucQueryExpression instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucQueryExpression since parent returns ARObject
        return cast("EcucQueryExpression", obj)


class EcucQueryExpressionBuilder:
    """Builder for EcucQueryExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucQueryExpression = EcucQueryExpression()

    def build(self) -> EcucQueryExpression:
        """Build and return EcucQueryExpression object.

        Returns:
            EcucQueryExpression instance
        """
        # TODO: Add validation
        return self._obj
