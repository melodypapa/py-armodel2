"""ExecutionTimeConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionTimeConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ExecutionTimeConstraint(TimingConstraint):
    """AUTOSAR ExecutionTimeConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "component": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # component
        "executable_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExecutableEntity,
        ),  # executableEntity
        "execution_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExecutionTimeTypeEnum,
        ),  # executionTime
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # maximum
        "minimum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # minimum
    }

    def __init__(self) -> None:
        """Initialize ExecutionTimeConstraint."""
        super().__init__()
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.execution_time: Optional[ExecutionTimeTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None


class ExecutionTimeConstraintBuilder:
    """Builder for ExecutionTimeConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionTimeConstraint = ExecutionTimeConstraint()

    def build(self) -> ExecutionTimeConstraint:
        """Build and return ExecutionTimeConstraint object.

        Returns:
            ExecutionTimeConstraint instance
        """
        # TODO: Add validation
        return self._obj
