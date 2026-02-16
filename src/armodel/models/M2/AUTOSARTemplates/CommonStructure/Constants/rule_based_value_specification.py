"""RuleBasedValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_arguments import (
    RuleArguments,
)


class RuleBasedValueSpecification(ARObject):
    """AUTOSAR RuleBasedValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, False, RuleArguments),  # arguments
        ("max_size_to_fill", None, True, False, None),  # maxSizeToFill
        ("rule", None, True, False, None),  # rule
    ]

    def __init__(self) -> None:
        """Initialize RuleBasedValueSpecification."""
        super().__init__()
        self.arguments: Optional[RuleArguments] = None
        self.max_size_to_fill: Optional[Integer] = None
        self.rule: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RuleBasedValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueSpecification":
        """Create RuleBasedValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RuleBasedValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RuleBasedValueSpecification since parent returns ARObject
        return cast("RuleBasedValueSpecification", obj)


class RuleBasedValueSpecificationBuilder:
    """Builder for RuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedValueSpecification = RuleBasedValueSpecification()

    def build(self) -> RuleBasedValueSpecification:
        """Build and return RuleBasedValueSpecification object.

        Returns:
            RuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
