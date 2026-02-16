"""AnalyzedExecutionTime AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class AnalyzedExecutionTime(ExecutionTime):
    """AUTOSAR AnalyzedExecutionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "best_case": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # bestCase
        "worst_case": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # worstCase
    }

    def __init__(self) -> None:
        """Initialize AnalyzedExecutionTime."""
        super().__init__()
        self.best_case: Optional[MultidimensionalTime] = None
        self.worst_case: Optional[MultidimensionalTime] = None


class AnalyzedExecutionTimeBuilder:
    """Builder for AnalyzedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AnalyzedExecutionTime = AnalyzedExecutionTime()

    def build(self) -> AnalyzedExecutionTime:
        """Build and return AnalyzedExecutionTime object.

        Returns:
            AnalyzedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
