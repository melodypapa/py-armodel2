"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    controlled_hw: Optional[HwElement]
    ecu_instance: Optional[EcuInstance]
    processing_unit: Optional[HwElement]
    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.processing_unit: Optional[HwElement] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Deserialize XML element to SwcToEcuMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToEcuMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse components (list)
        obj.components = []
        for child in ARObject._find_all_child_elements(element, "COMPONENTS"):
            components_value = child.text
            obj.components.append(components_value)

        # Parse controlled_hw
        child = ARObject._find_child_element(element, "CONTROLLED-HW")
        if child is not None:
            controlled_hw_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.controlled_hw = controlled_hw_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse processing_unit
        child = ARObject._find_child_element(element, "PROCESSING-UNIT")
        if child is not None:
            processing_unit_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.processing_unit = processing_unit_value

        return obj



class SwcToEcuMappingBuilder:
    """Builder for SwcToEcuMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToEcuMapping = SwcToEcuMapping()

    def build(self) -> SwcToEcuMapping:
        """Build and return SwcToEcuMapping object.

        Returns:
            SwcToEcuMapping instance
        """
        # TODO: Add validation
        return self._obj
