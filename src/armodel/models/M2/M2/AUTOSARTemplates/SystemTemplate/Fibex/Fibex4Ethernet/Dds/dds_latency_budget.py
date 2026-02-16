"""DdsLatencyBudget AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLatencyBudget(ARObject):
    """AUTOSAR DdsLatencyBudget."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "latency_budget": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # latencyBudget
    }

    def __init__(self) -> None:
        """Initialize DdsLatencyBudget."""
        super().__init__()
        self.latency_budget: Optional[Float] = None


class DdsLatencyBudgetBuilder:
    """Builder for DdsLatencyBudget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLatencyBudget = DdsLatencyBudget()

    def build(self) -> DdsLatencyBudget:
        """Build and return DdsLatencyBudget object.

        Returns:
            DdsLatencyBudget instance
        """
        # TODO: Add validation
        return self._obj
