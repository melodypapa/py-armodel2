"""NumericalRuleBasedValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR NumericalRuleBasedValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rule_based", None, False, False, any (RuleBasedValue)),  # ruleBased
    ]

    def __init__(self) -> None:
        """Initialize NumericalRuleBasedValueSpecification."""
        super().__init__()
        self.rule_based: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NumericalRuleBasedValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalRuleBasedValueSpecification":
        """Create NumericalRuleBasedValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NumericalRuleBasedValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NumericalRuleBasedValueSpecification since parent returns ARObject
        return cast("NumericalRuleBasedValueSpecification", obj)


class NumericalRuleBasedValueSpecificationBuilder:
    """Builder for NumericalRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalRuleBasedValueSpecification = NumericalRuleBasedValueSpecification()

    def build(self) -> NumericalRuleBasedValueSpecification:
        """Build and return NumericalRuleBasedValueSpecification object.

        Returns:
            NumericalRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
