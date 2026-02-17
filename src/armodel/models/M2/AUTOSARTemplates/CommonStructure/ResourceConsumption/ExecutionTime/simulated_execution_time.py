"""SimulatedExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 167)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SimulatedExecutionTime(ExecutionTime):
    """AUTOSAR SimulatedExecutionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "maximum_execution_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # maximumExecutionTime
        "minimum_execution_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # minimumExecutionTime
        "nominal_execution_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # nominalExecutionTime
    }

    def __init__(self) -> None:
        """Initialize SimulatedExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None


class SimulatedExecutionTimeBuilder:
    """Builder for SimulatedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SimulatedExecutionTime = SimulatedExecutionTime()

    def build(self) -> SimulatedExecutionTime:
        """Build and return SimulatedExecutionTime object.

        Returns:
            SimulatedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
