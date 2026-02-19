"""InitialSdDelayConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 514)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_delay_max: Optional[TimeValue]
    initial_delay_min: Optional[TimeValue]
    initial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitialSdDelayConfig":
        """Deserialize XML element to InitialSdDelayConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InitialSdDelayConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse initial_delay_max
        child = ARObject._find_child_element(element, "INITIAL-DELAY-MAX")
        if child is not None:
            initial_delay_max_value = child.text
            obj.initial_delay_max = initial_delay_max_value

        # Parse initial_delay_min
        child = ARObject._find_child_element(element, "INITIAL-DELAY-MIN")
        if child is not None:
            initial_delay_min_value = child.text
            obj.initial_delay_min = initial_delay_min_value

        # Parse initial
        child = ARObject._find_child_element(element, "INITIAL")
        if child is not None:
            initial_value = child.text
            obj.initial = initial_value

        return obj



class InitialSdDelayConfigBuilder:
    """Builder for InitialSdDelayConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()

    def build(self) -> InitialSdDelayConfig:
        """Build and return InitialSdDelayConfig object.

        Returns:
            InitialSdDelayConfig instance
        """
        # TODO: Add validation
        return self._obj
