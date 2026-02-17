"""CycleRepetition AUTOSAR element.

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


class CycleRepetition(CommunicationCycle):
    """AUTOSAR CycleRepetition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # BaseCycle
        "cycle_repetition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CycleRepetitionType,
        ),  # CycleRepetition
    }

    def __init__(self) -> None:
        """Initialize CycleRepetition."""
        super().__init__()
        self.base_cycle: Optional[Integer] = None
        self.cycle_repetition: Optional[CycleRepetitionType] = None


class CycleRepetitionBuilder:
    """Builder for CycleRepetition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CycleRepetition = CycleRepetition()

    def build(self) -> CycleRepetition:
        """Build and return CycleRepetition object.

        Returns:
            CycleRepetition instance
        """
        # TODO: Add validation
        return self._obj
