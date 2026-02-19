"""ApplicationRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 462)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_rule_based_value_argument import (
    CompositeRuleBasedValueArgument,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category_specification: Optional[Identifier]
    sw_axis_conts: list[RuleBasedAxisCont]
    sw_value_cont: Optional[RuleBasedValueCont]
    def __init__(self) -> None:
        """Initialize ApplicationRuleBasedValueSpecification."""
        super().__init__()
        self.category_specification: Optional[Identifier] = None
        self.sw_axis_conts: list[RuleBasedAxisCont] = []
        self.sw_value_cont: Optional[RuleBasedValueCont] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRuleBasedValueSpecification":
        """Deserialize XML element to ApplicationRuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRuleBasedValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRuleBasedValueSpecification, cls).deserialize(element)

        # Parse category_specification
        child = ARObject._find_child_element(element, "CATEGORY-SPECIFICATION")
        if child is not None:
            category_specification_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.category_specification = category_specification_value

        # Parse sw_axis_conts (list from container "SW-AXIS-CONTS")
        obj.sw_axis_conts = []
        container = ARObject._find_child_element(element, "SW-AXIS-CONTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_axis_conts.append(child_value)

        # Parse sw_value_cont
        child = ARObject._find_child_element(element, "SW-VALUE-CONT")
        if child is not None:
            sw_value_cont_value = ARObject._deserialize_by_tag(child, "RuleBasedValueCont")
            obj.sw_value_cont = sw_value_cont_value

        return obj



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
