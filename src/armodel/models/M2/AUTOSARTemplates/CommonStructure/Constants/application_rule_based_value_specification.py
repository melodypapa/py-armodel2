"""ApplicationRuleBasedValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_rule_based_value_argument import (
    CompositeRuleBasedValueArgument,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_based_axis_cont import (
    RuleBasedAxisCont,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_based_value_cont import (
    RuleBasedValueCont,
)


class ApplicationRuleBasedValueSpecification(CompositeRuleBasedValueArgument):
    """AUTOSAR ApplicationRuleBasedValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category_specification", None, True, False, None),  # categorySpecification
        ("sw_axis_conts", None, False, True, RuleBasedAxisCont),  # swAxisConts
        ("sw_value_cont", None, False, False, RuleBasedValueCont),  # swValueCont
    ]

    def __init__(self) -> None:
        """Initialize ApplicationRuleBasedValueSpecification."""
        super().__init__()
        self.category_specification: Optional[Identifier] = None
        self.sw_axis_conts: list[RuleBasedAxisCont] = []
        self.sw_value_cont: Optional[RuleBasedValueCont] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationRuleBasedValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRuleBasedValueSpecification":
        """Create ApplicationRuleBasedValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationRuleBasedValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationRuleBasedValueSpecification since parent returns ARObject
        return cast("ApplicationRuleBasedValueSpecification", obj)


class ApplicationRuleBasedValueSpecificationBuilder:
    """Builder for ApplicationRuleBasedValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRuleBasedValueSpecification = ApplicationRuleBasedValueSpecification()

    def build(self) -> ApplicationRuleBasedValueSpecification:
        """Build and return ApplicationRuleBasedValueSpecification object.

        Returns:
            ApplicationRuleBasedValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
