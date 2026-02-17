"""CycleCounter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CycleCounter(CommunicationCycle):
    """AUTOSAR CycleCounter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cycle_counter": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # CycleCounter
    }

    def __init__(self) -> None:
        """Initialize CycleCounter."""
        super().__init__()
        self.cycle_counter: Optional[Integer] = None


class CycleCounterBuilder:
    """Builder for CycleCounter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CycleCounter = CycleCounter()

    def build(self) -> CycleCounter:
        """Build and return CycleCounter object.

        Returns:
            CycleCounter instance
        """
        # TODO: Add validation
        return self._obj
