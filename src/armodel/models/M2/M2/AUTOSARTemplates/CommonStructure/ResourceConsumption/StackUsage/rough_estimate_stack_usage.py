"""RoughEstimateStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 151)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RoughEstimateStackUsage(StackUsage):
    """AUTOSAR RoughEstimateStackUsage."""

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
        """Initialize RoughEstimateStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class RoughEstimateStackUsageBuilder:
    """Builder for RoughEstimateStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateStackUsage = RoughEstimateStackUsage()

    def build(self) -> RoughEstimateStackUsage:
        """Build and return RoughEstimateStackUsage object.

        Returns:
            RoughEstimateStackUsage instance
        """
        # TODO: Add validation
        return self._obj
