"""ExecutableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 538)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2024)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ReentrancyLevelEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)
from abc import ABC, abstractmethod


class ExecutableEntity(Identifiable, ABC):
    """AUTOSAR ExecutableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    activations: list[ExecutableEntity]
    can_enters: list[ExclusiveArea]
    exclusive_area_nestings: list[ExclusiveAreaNestingOrder]
    minimum_start: Optional[TimeValue]
    reentrancy_level_enum: Optional[ReentrancyLevelEnum]
    runs_insides: list[ExclusiveArea]
    sw_addr_method: Optional[SwAddrMethod]
    def __init__(self) -> None:
        """Initialize ExecutableEntity."""
        super().__init__()
        self.activations: list[ExecutableEntity] = []
        self.can_enters: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.minimum_start: Optional[TimeValue] = None
        self.reentrancy_level_enum: Optional[ReentrancyLevelEnum] = None
        self.runs_insides: list[ExclusiveArea] = []
        self.sw_addr_method: Optional[SwAddrMethod] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntity":
        """Deserialize XML element to ExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse activations (list)
        obj.activations = []
        for child in ARObject._find_all_child_elements(element, "ACTIVATIONS"):
            activations_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.activations.append(activations_value)

        # Parse can_enters (list)
        obj.can_enters = []
        for child in ARObject._find_all_child_elements(element, "CAN-ENTERS"):
            can_enters_value = ARObject._deserialize_by_tag(child, "ExclusiveArea")
            obj.can_enters.append(can_enters_value)

        # Parse exclusive_area_nestings (list)
        obj.exclusive_area_nestings = []
        for child in ARObject._find_all_child_elements(element, "EXCLUSIVE-AREA-NESTINGS"):
            exclusive_area_nestings_value = ARObject._deserialize_by_tag(child, "ExclusiveAreaNestingOrder")
            obj.exclusive_area_nestings.append(exclusive_area_nestings_value)

        # Parse minimum_start
        child = ARObject._find_child_element(element, "MINIMUM-START")
        if child is not None:
            minimum_start_value = child.text
            obj.minimum_start = minimum_start_value

        # Parse reentrancy_level_enum
        child = ARObject._find_child_element(element, "REENTRANCY-LEVEL-ENUM")
        if child is not None:
            reentrancy_level_enum_value = child.text
            obj.reentrancy_level_enum = reentrancy_level_enum_value

        # Parse runs_insides (list)
        obj.runs_insides = []
        for child in ARObject._find_all_child_elements(element, "RUNS-INSIDES"):
            runs_insides_value = ARObject._deserialize_by_tag(child, "ExclusiveArea")
            obj.runs_insides.append(runs_insides_value)

        # Parse sw_addr_method
        child = ARObject._find_child_element(element, "SW-ADDR-METHOD")
        if child is not None:
            sw_addr_method_value = ARObject._deserialize_by_tag(child, "SwAddrMethod")
            obj.sw_addr_method = sw_addr_method_value

        return obj



class ExecutableEntityBuilder:
    """Builder for ExecutableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutableEntity = ExecutableEntity()

    def build(self) -> ExecutableEntity:
        """Build and return ExecutableEntity object.

        Returns:
            ExecutableEntity instance
        """
        # TODO: Add validation
        return self._obj
