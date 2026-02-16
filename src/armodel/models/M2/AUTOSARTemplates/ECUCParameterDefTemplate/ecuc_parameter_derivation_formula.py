"""EcucParameterDerivationFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)


class EcucParameterDerivationFormula(ARObject):
    """AUTOSAR EcucParameterDerivationFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_query", None, False, False, EcucQuery),  # ecucQuery
    ]

    def __init__(self) -> None:
        """Initialize EcucParameterDerivationFormula."""
        super().__init__()
        self.ecuc_query: Optional[EcucQuery] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucParameterDerivationFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDerivationFormula":
        """Create EcucParameterDerivationFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucParameterDerivationFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucParameterDerivationFormula since parent returns ARObject
        return cast("EcucParameterDerivationFormula", obj)


class EcucParameterDerivationFormulaBuilder:
    """Builder for EcucParameterDerivationFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDerivationFormula = EcucParameterDerivationFormula()

    def build(self) -> EcucParameterDerivationFormula:
        """Build and return EcucParameterDerivationFormula object.

        Returns:
            EcucParameterDerivationFormula instance
        """
        # TODO: Add validation
        return self._obj
