"""WorstCaseStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class WorstCaseStackUsage(StackUsage):
    """AUTOSAR WorstCaseStackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory_consumption: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize WorstCaseStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "WorstCaseStackUsage":
        """Deserialize XML element to WorstCaseStackUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WorstCaseStackUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WorstCaseStackUsage, cls).deserialize(element)

        # Parse memory_consumption
        child = ARObject._find_child_element(element, "MEMORY-CONSUMPTION")
        if child is not None:
            memory_consumption_value = child.text
            obj.memory_consumption = memory_consumption_value

        return obj



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
