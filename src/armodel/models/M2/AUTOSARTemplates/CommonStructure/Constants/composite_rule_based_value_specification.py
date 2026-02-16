"""CompositeRuleBasedValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR CompositeRuleBasedValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, CompositeValueSpecification),  # arguments
        ("compounds", None, False, True, any (CompositeRuleBased)),  # compounds
        ("max_size_to_fill", None, True, False, None),  # maxSizeToFill
        ("rule", None, True, False, None),  # rule
    ]

    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueSpecification."""
        super().__init__()
        self.arguments: list[CompositeValueSpecification] = []
        self.compounds: list[Any] = []
        self.max_size_to_fill: Optional[PositiveInteger] = None
        self.rule: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompositeRuleBasedValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeRuleBasedValueSpecification":
        """Create CompositeRuleBasedValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompositeRuleBasedValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompositeRuleBasedValueSpecification since parent returns ARObject
        return cast("CompositeRuleBasedValueSpecification", obj)


class CompositeRuleBasedValueSpecificationBuilder:
    """Builder for CompositeRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeRuleBasedValueSpecification = CompositeRuleBasedValueSpecification()

    def build(self) -> CompositeRuleBasedValueSpecification:
        """Build and return CompositeRuleBasedValueSpecification object.

        Returns:
            CompositeRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
