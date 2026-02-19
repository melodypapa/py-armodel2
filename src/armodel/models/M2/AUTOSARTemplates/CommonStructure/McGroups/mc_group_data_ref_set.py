"""McGroupDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 191)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2035)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

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


class McGroupDataRefSet(ARObject):
    """AUTOSAR McGroupDataRefSet."""

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
        """Initialize McGroupDataRefSet."""
        super().__init__()
        self.flat_map_entries: list[FlatInstanceDescriptor] = []
        self.mc_data_instances: list[McDataInstance] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroupDataRefSet":
        """Deserialize XML element to McGroupDataRefSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroupDataRefSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse flat_map_entries (list)
        obj.flat_map_entries = []
        for child in ARObject._find_all_child_elements(element, "FLAT-MAP-ENTRIES"):
            flat_map_entries_value = ARObject._deserialize_by_tag(child, "FlatInstanceDescriptor")
            obj.flat_map_entries.append(flat_map_entries_value)

        # Parse mc_data_instances (list)
        obj.mc_data_instances = []
        for child in ARObject._find_all_child_elements(element, "MC-DATA-INSTANCES"):
            mc_data_instances_value = ARObject._deserialize_by_tag(child, "McDataInstance")
            obj.mc_data_instances.append(mc_data_instances_value)

        return obj



class McGroupDataRefSetBuilder:
    """Builder for McGroupDataRefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McGroupDataRefSet = McGroupDataRefSet()

    def build(self) -> McGroupDataRefSet:
        """Build and return McGroupDataRefSet object.

        Returns:
            McGroupDataRefSet instance
        """
        # TODO: Add validation
        return self._obj
