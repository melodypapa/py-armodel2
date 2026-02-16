"""McFunctionDataRefSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class McFunctionDataRefSet(ARObject):
    """AUTOSAR McFunctionDataRefSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("flat_map_entries", None, False, True, FlatInstanceDescriptor),  # flatMapEntries
        ("mc_data_instances", None, False, True, McDataInstance),  # mcDataInstances
    ]

    def __init__(self) -> None:
        """Initialize McFunctionDataRefSet."""
        super().__init__()
        self.flat_map_entries: list[FlatInstanceDescriptor] = []
        self.mc_data_instances: list[McDataInstance] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McFunctionDataRefSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunctionDataRefSet":
        """Create McFunctionDataRefSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McFunctionDataRefSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McFunctionDataRefSet since parent returns ARObject
        return cast("McFunctionDataRefSet", obj)


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
