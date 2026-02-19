"""ClassContentConditional AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
    SdgTailoring,
)


class ClassContentConditional(Identifiable):
    """AUTOSAR ClassContentConditional."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[AttributeTailoring]
    condition: Optional[AbstractCondition]
    constraints: list[ConstraintTailoring]
    sdg_tailorings: list[SdgTailoring]
    def __init__(self) -> None:
        """Initialize ClassContentConditional."""
        super().__init__()
        self.attributes: list[AttributeTailoring] = []
        self.condition: Optional[AbstractCondition] = None
        self.constraints: list[ConstraintTailoring] = []
        self.sdg_tailorings: list[SdgTailoring] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassContentConditional":
        """Deserialize XML element to ClassContentConditional object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClassContentConditional object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClassContentConditional, cls).deserialize(element)

        # Parse attributes (list from container "ATTRIBUTES")
        obj.attributes = []
        container = ARObject._find_child_element(element, "ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attributes.append(child_value)

        # Parse condition
        child = ARObject._find_child_element(element, "CONDITION")
        if child is not None:
            condition_value = ARObject._deserialize_by_tag(child, "AbstractCondition")
            obj.condition = condition_value

        # Parse constraints (list from container "CONSTRAINTS")
        obj.constraints = []
        container = ARObject._find_child_element(element, "CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constraints.append(child_value)

        # Parse sdg_tailorings (list from container "SDG-TAILORINGS")
        obj.sdg_tailorings = []
        container = ARObject._find_child_element(element, "SDG-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdg_tailorings.append(child_value)

        return obj



class ClassContentConditionalBuilder:
    """Builder for ClassContentConditional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassContentConditional = ClassContentConditional()

    def build(self) -> ClassContentConditional:
        """Build and return ClassContentConditional object.

        Returns:
            ClassContentConditional instance
        """
        # TODO: Add validation
        return self._obj
