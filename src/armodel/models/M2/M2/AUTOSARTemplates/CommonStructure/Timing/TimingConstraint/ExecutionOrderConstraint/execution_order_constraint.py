"""ExecutionOrderConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # base
        "execution_order": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # executionOrder
        "ignore_order": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ignoreOrder
        "is_event": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isEvent
        "ordered_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # orderedElements
        "permit_multiple": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # permitMultiple
    }

    def __init__(self) -> None:
        """Initialize ExecutionOrderConstraint."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.execution_order: Optional[Any] = None
        self.ignore_order: Optional[Boolean] = None
        self.is_event: Optional[Boolean] = None
        self.ordered_elements: list[Any] = []
        self.permit_multiple: Optional[Boolean] = None


class ExecutionOrderConstraintBuilder:
    """Builder for ExecutionOrderConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()

    def build(self) -> ExecutionOrderConstraint:
        """Build and return ExecutionOrderConstraint object.

        Returns:
            ExecutionOrderConstraint instance
        """
        # TODO: Add validation
        return self._obj
