"""WorstCaseStackUsage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class WorstCaseStackUsage(StackUsage):
    """AUTOSAR WorstCaseStackUsage."""

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
        """Initialize WorstCaseStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None


class WorstCaseStackUsageBuilder:
    """Builder for WorstCaseStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WorstCaseStackUsage = WorstCaseStackUsage()

    def build(self) -> WorstCaseStackUsage:
        """Build and return WorstCaseStackUsage object.

        Returns:
            WorstCaseStackUsage instance
        """
        # TODO: Add validation
        return self._obj
