"""CycleCounter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CycleCounter(CommunicationCycle):
    """AUTOSAR CycleCounter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cycle_counter: Optional[Integer]
    def __init__(self) -> None:
        """Initialize CycleCounter."""
        super().__init__()
        self.cycle_counter: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleCounter":
        """Deserialize XML element to CycleCounter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CycleCounter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CycleCounter, cls).deserialize(element)

        # Parse cycle_counter
        child = ARObject._find_child_element(element, "CYCLE-COUNTER")
        if child is not None:
            cycle_counter_value = child.text
            obj.cycle_counter = cycle_counter_value

        return obj



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
