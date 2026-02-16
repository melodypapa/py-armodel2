"""WorstCaseHeapUsage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class WorstCaseHeapUsage(HeapUsage):
    """AUTOSAR WorstCaseHeapUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "memory_consumption": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # memoryConsumption
    }

    def __init__(self) -> None:
        """Initialize WorstCaseHeapUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class WorstCaseHeapUsageBuilder:
    """Builder for WorstCaseHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WorstCaseHeapUsage = WorstCaseHeapUsage()

    def build(self) -> WorstCaseHeapUsage:
        """Build and return WorstCaseHeapUsage object.

        Returns:
            WorstCaseHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
