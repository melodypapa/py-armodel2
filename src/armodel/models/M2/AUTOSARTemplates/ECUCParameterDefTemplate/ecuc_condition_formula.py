"""EcucConditionFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)


class EcucConditionFormula(ARObject):
    """AUTOSAR EcucConditionFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_query", None, False, False, EcucQuery),  # ecucQuery
    ]

    def __init__(self) -> None:
        """Initialize EcucConditionFormula."""
        super().__init__()
        self.ecuc_query: Optional[EcucQuery] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucConditionFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucConditionFormula":
        """Create EcucConditionFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucConditionFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucConditionFormula since parent returns ARObject
        return cast("EcucConditionFormula", obj)


class EcucConditionFormulaBuilder:
    """Builder for EcucConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucConditionFormula = EcucConditionFormula()

    def build(self) -> EcucConditionFormula:
        """Build and return EcucConditionFormula object.

        Returns:
            EcucConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
