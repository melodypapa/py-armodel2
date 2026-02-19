"""McFunctionDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 187)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class McFunctionDataRefSet(ARObject):
    """AUTOSAR McFunctionDataRefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_map_entries: list[FlatInstanceDescriptor]
    mc_data_instances: list[McDataInstance]
    def __init__(self) -> None:
        """Initialize McFunctionDataRefSet."""
        super().__init__()
        self.flat_map_entries: list[FlatInstanceDescriptor] = []
        self.mc_data_instances: list[McDataInstance] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunctionDataRefSet":
        """Deserialize XML element to McFunctionDataRefSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McFunctionDataRefSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse flat_map_entries (list from container "FLAT-MAP-ENTRIES")
        obj.flat_map_entries = []
        container = ARObject._find_child_element(element, "FLAT-MAP-ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flat_map_entries.append(child_value)

        # Parse mc_data_instances (list from container "MC-DATA-INSTANCES")
        obj.mc_data_instances = []
        container = ARObject._find_child_element(element, "MC-DATA-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_data_instances.append(child_value)

        return obj



class McFunctionDataRefSetBuilder:
    """Builder for McFunctionDataRefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McFunctionDataRefSet = McFunctionDataRefSet()

    def build(self) -> McFunctionDataRefSet:
        """Build and return McFunctionDataRefSet object.

        Returns:
            McFunctionDataRefSet instance
        """
        # TODO: Add validation
        return self._obj
