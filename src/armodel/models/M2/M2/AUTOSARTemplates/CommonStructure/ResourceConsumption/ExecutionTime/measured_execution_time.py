"""MeasuredExecutionTime AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class MeasuredExecutionTime(ExecutionTime):
    """AUTOSAR MeasuredExecutionTime."""

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
        """Initialize MeasuredExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None


class MeasuredExecutionTimeBuilder:
    """Builder for MeasuredExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredExecutionTime = MeasuredExecutionTime()

    def build(self) -> MeasuredExecutionTime:
        """Build and return MeasuredExecutionTime object.

        Returns:
            MeasuredExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
