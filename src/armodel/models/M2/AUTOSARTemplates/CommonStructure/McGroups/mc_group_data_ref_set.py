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
    def serialize(self) -> ET.Element:
        """Serialize McGroupDataRefSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize flat_map_entries (list to container "FLAT-MAP-ENTRIES")
        if self.flat_map_entries:
            wrapper = ET.Element("FLAT-MAP-ENTRIES")
            for item in self.flat_map_entries:
                serialized = ARObject._serialize_item(item, "FlatInstanceDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_data_instances (list to container "MC-DATA-INSTANCES")
        if self.mc_data_instances:
            wrapper = ET.Element("MC-DATA-INSTANCES")
            for item in self.mc_data_instances:
                serialized = ARObject._serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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
