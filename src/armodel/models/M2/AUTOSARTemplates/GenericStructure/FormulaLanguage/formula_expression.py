"""FormulaExpression AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class FormulaExpression(ARObject):
    """AUTOSAR FormulaExpression."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("atp_references", None, False, True, Referrable),  # atpReferences
        ("atp_strings", None, False, True, Referrable),  # atpStrings
    ]

    def __init__(self) -> None:
        """Initialize FormulaExpression."""
        super().__init__()
        self.atp_references: list[Referrable] = []
        self.atp_strings: list[Referrable] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FormulaExpression to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FormulaExpression":
        """Create FormulaExpression from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FormulaExpression instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FormulaExpression since parent returns ARObject
        return cast("FormulaExpression", obj)


class FormulaExpressionBuilder:
    """Builder for FormulaExpression."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FormulaExpression = FormulaExpression()

    def build(self) -> FormulaExpression:
        """Build and return FormulaExpression object.

        Returns:
            FormulaExpression instance
        """
        # TODO: Add validation
        return self._obj
