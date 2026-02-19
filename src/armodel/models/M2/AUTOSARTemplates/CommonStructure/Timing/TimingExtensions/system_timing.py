"""SystemTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class SystemTiming(TimingExtension):
    """AUTOSAR SystemTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system: Optional[System]
    def __init__(self) -> None:
        """Initialize SystemTiming."""
        super().__init__()
        self.system: Optional[System] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemTiming":
        """Deserialize XML element to SystemTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse system
        child = ARObject._find_child_element(element, "SYSTEM")
        if child is not None:
            system_value = ARObject._deserialize_by_tag(child, "System")
            obj.system = system_value

        return obj



class SystemTimingBuilder:
    """Builder for SystemTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemTiming = SystemTiming()

    def build(self) -> SystemTiming:
        """Build and return SystemTiming object.

        Returns:
            SystemTiming instance
        """
        # TODO: Add validation
        return self._obj
