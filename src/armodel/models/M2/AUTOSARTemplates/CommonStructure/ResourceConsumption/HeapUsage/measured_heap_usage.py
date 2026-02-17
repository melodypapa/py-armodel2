"""MeasuredHeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_HeapUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredHeapUsage(HeapUsage):
    """AUTOSAR MeasuredHeapUsage."""

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
        """Initialize MeasuredHeapUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None


class MeasuredHeapUsageBuilder:
    """Builder for MeasuredHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredHeapUsage = MeasuredHeapUsage()

    def build(self) -> MeasuredHeapUsage:
        """Build and return MeasuredHeapUsage object.

        Returns:
            MeasuredHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
