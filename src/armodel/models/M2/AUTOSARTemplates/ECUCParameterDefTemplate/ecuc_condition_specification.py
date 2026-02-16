"""EcucConditionSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
    EcucConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)


class EcucConditionSpecification(ARObject):
    """AUTOSAR EcucConditionSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("condition", None, False, False, EcucConditionFormula),  # condition
        ("ecuc_queries", None, False, True, EcucQuery),  # ecucQueries
        ("informal_formula", None, False, False, MlFormula),  # informalFormula
    ]

    def __init__(self) -> None:
        """Initialize EcucConditionSpecification."""
        super().__init__()
        self.condition: Optional[EcucConditionFormula] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucConditionSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucConditionSpecification":
        """Create EcucConditionSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucConditionSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucConditionSpecification since parent returns ARObject
        return cast("EcucConditionSpecification", obj)


class EcucConditionSpecificationBuilder:
    """Builder for EcucConditionSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucConditionSpecification = EcucConditionSpecification()

    def build(self) -> EcucConditionSpecification:
        """Build and return EcucConditionSpecification object.

        Returns:
            EcucConditionSpecification instance
        """
        # TODO: Add validation
        return self._obj
