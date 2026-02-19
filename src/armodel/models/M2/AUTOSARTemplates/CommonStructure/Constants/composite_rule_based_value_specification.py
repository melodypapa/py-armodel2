"""CompositeRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR CompositeRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[CompositeValueSpecification]
    compounds: list[Any]
    max_size_to_fill: Optional[PositiveInteger]
    rule: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueSpecification."""
        super().__init__()
        self.arguments: list[CompositeValueSpecification] = []
        self.compounds: list[Any] = []
        self.max_size_to_fill: Optional[PositiveInteger] = None
        self.rule: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeRuleBasedValueSpecification":
        """Deserialize XML element to CompositeRuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompositeRuleBasedValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arguments (list)
        obj.arguments = []
        for child in ARObject._find_all_child_elements(element, "ARGUMENTS"):
            arguments_value = ARObject._deserialize_by_tag(child, "CompositeValueSpecification")
            obj.arguments.append(arguments_value)

        # Parse compounds (list)
        obj.compounds = []
        for child in ARObject._find_all_child_elements(element, "COMPOUNDS"):
            compounds_value = child.text
            obj.compounds.append(compounds_value)

        # Parse max_size_to_fill
        child = ARObject._find_child_element(element, "MAX-SIZE-TO-FILL")
        if child is not None:
            max_size_to_fill_value = child.text
            obj.max_size_to_fill = max_size_to_fill_value

        # Parse rule
        child = ARObject._find_child_element(element, "RULE")
        if child is not None:
            rule_value = child.text
            obj.rule = rule_value

        return obj



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
