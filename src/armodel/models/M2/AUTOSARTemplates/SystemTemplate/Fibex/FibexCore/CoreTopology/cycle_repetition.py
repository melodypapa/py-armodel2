"""CycleRepetition AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CycleRepetitionType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CycleRepetition(CommunicationCycle):
    """AUTOSAR CycleRepetition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_cycle: Optional[Integer]
    cycle_repetition: Optional[CycleRepetitionType]
    def __init__(self) -> None:
        """Initialize CycleRepetition."""
        super().__init__()
        self.base_cycle: Optional[Integer] = None
        self.cycle_repetition: Optional[CycleRepetitionType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleRepetition":
        """Deserialize XML element to CycleRepetition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CycleRepetition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_cycle
        child = ARObject._find_child_element(element, "BASE-CYCLE")
        if child is not None:
            base_cycle_value = child.text
            obj.base_cycle = base_cycle_value

        # Parse cycle_repetition
        child = ARObject._find_child_element(element, "CYCLE-REPETITION")
        if child is not None:
            cycle_repetition_value = child.text
            obj.cycle_repetition = cycle_repetition_value

        return obj



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
