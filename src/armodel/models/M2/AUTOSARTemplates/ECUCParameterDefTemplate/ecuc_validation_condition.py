"""EcucValidationCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
    EcucConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)


class EcucValidationCondition(Identifiable):
    """AUTOSAR EcucValidationCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_queries", None, False, True, EcucQuery),  # ecucQueries
        ("validation", None, False, False, EcucConditionFormula),  # validation
    ]

    def __init__(self) -> None:
        """Initialize EcucValidationCondition."""
        super().__init__()
        self.ecuc_queries: list[EcucQuery] = []
        self.validation: Optional[EcucConditionFormula] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucValidationCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValidationCondition":
        """Create EcucValidationCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucValidationCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucValidationCondition since parent returns ARObject
        return cast("EcucValidationCondition", obj)


class EcucValidationConditionBuilder:
    """Builder for EcucValidationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValidationCondition = EcucValidationCondition()

    def build(self) -> EcucValidationCondition:
        """Build and return EcucValidationCondition object.

        Returns:
            EcucValidationCondition instance
        """
        # TODO: Add validation
        return self._obj
