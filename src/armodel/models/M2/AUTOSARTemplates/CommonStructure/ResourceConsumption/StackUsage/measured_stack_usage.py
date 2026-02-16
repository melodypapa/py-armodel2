"""MeasuredStackUsage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredStackUsage(StackUsage):
    """AUTOSAR MeasuredStackUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "average_memory_consumption": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # averageMemoryConsumption
        "maximum_memory_consumption": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximumMemoryConsumption
        "minimum_memory_consumption": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minimumMemoryConsumption
        "test_pattern": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # testPattern
    }

    def __init__(self) -> None:
        """Initialize MeasuredStackUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None


class MeasuredStackUsageBuilder:
    """Builder for MeasuredStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredStackUsage = MeasuredStackUsage()

    def build(self) -> MeasuredStackUsage:
        """Build and return MeasuredStackUsage object.

        Returns:
            MeasuredStackUsage instance
        """
        # TODO: Add validation
        return self._obj
