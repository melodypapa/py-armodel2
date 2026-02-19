"""SupervisedEntityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 707)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activate_at_start: Optional[Boolean]
    checkpointses: list[Any]
    enable: Optional[Boolean]
    expected_alive: Optional[TimeValue]
    max_alive_cycle: Optional[TimeValue]
    min_alive_cycle: Optional[TimeValue]
    tolerated_failed: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpointses: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SupervisedEntityNeeds":
        """Deserialize XML element to SupervisedEntityNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SupervisedEntityNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse activate_at_start
        child = ARObject._find_child_element(element, "ACTIVATE-AT-START")
        if child is not None:
            activate_at_start_value = child.text
            obj.activate_at_start = activate_at_start_value

        # Parse checkpointses (list)
        obj.checkpointses = []
        for child in ARObject._find_all_child_elements(element, "CHECKPOINTSES"):
            checkpointses_value = child.text
            obj.checkpointses.append(checkpointses_value)

        # Parse enable
        child = ARObject._find_child_element(element, "ENABLE")
        if child is not None:
            enable_value = child.text
            obj.enable = enable_value

        # Parse expected_alive
        child = ARObject._find_child_element(element, "EXPECTED-ALIVE")
        if child is not None:
            expected_alive_value = child.text
            obj.expected_alive = expected_alive_value

        # Parse max_alive_cycle
        child = ARObject._find_child_element(element, "MAX-ALIVE-CYCLE")
        if child is not None:
            max_alive_cycle_value = child.text
            obj.max_alive_cycle = max_alive_cycle_value

        # Parse min_alive_cycle
        child = ARObject._find_child_element(element, "MIN-ALIVE-CYCLE")
        if child is not None:
            min_alive_cycle_value = child.text
            obj.min_alive_cycle = min_alive_cycle_value

        # Parse tolerated_failed
        child = ARObject._find_child_element(element, "TOLERATED-FAILED")
        if child is not None:
            tolerated_failed_value = child.text
            obj.tolerated_failed = tolerated_failed_value

        return obj



class SupervisedEntityNeedsBuilder:
    """Builder for SupervisedEntityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()

    def build(self) -> SupervisedEntityNeeds:
        """Build and return SupervisedEntityNeeds object.

        Returns:
            SupervisedEntityNeeds instance
        """
        # TODO: Add validation
        return self._obj
