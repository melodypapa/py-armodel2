"""RoughEstimateOfExecutionTime AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "additional": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # additional
        "estimated_execution_time": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # estimatedExecutionTime
    }

    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None


class RoughEstimateOfExecutionTimeBuilder:
    """Builder for RoughEstimateOfExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateOfExecutionTime = RoughEstimateOfExecutionTime()

    def build(self) -> RoughEstimateOfExecutionTime:
        """Build and return RoughEstimateOfExecutionTime object.

        Returns:
            RoughEstimateOfExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
