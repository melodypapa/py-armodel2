"""McGroupDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 191)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2035)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


@atp_variant()

class McGroupDataRefSet(ARObject):
    """AUTOSAR McGroupDataRefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_map_entrie_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McGroupDataRefSet."""
        super().__init__()
        self.flat_map_entrie_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McGroupDataRefSet to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize flat_map_entrie_refs (list from container "FLAT-MAP-ENTRIE-REFS")
        if self.flat_map_entrie_refs:
            container = ET.Element("FLAT-MAP-ENTRIE-REFS")
            for item in self.flat_map_entrie_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("FlatInstanceDescriptor", package_data):
                    # Simple primitive type
                    child = ET.Element("FLAT-MAP-ENTRIE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("FlatInstanceDescriptor", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        if self.mc_data_instance_refs:
            container = ET.Element("MC-DATA-INSTANCE-REFS")
            for item in self.mc_data_instance_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("McDataInstance", package_data):
                    # Simple primitive type
                    child = ET.Element("MC-DATA-INSTANCE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("McDataInstance", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "McGroupDataRefSet")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroupDataRefSet":
        """Deserialize XML element to McGroupDataRefSet object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroupDataRefSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "McGroupDataRefSet")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse flat_map_entrie_refs (list from container "FLAT-MAP-ENTRIE-REFS")
        obj.flat_map_entrie_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "FLAT-MAP-ENTRIE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("FlatInstanceDescriptor", package_data):
                    child_value = child.text
                elif is_enum_type("FlatInstanceDescriptor", package_data):
                    child_value = FlatInstanceDescriptor.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flat_map_entrie_refs.append(child_value)

        # Parse mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        obj.mc_data_instance_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "MC-DATA-INSTANCE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("McDataInstance", package_data):
                    child_value = child.text
                elif is_enum_type("McDataInstance", package_data):
                    child_value = McDataInstance.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_data_instance_refs.append(child_value)

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
