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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    can_enter_refs: list[ARRef]
    exclusive_area_nesting_refs: list[ARRef]
    minimum_start: Optional[TimeValue]
    reentrancy_level_enum: Optional[ReentrancyLevelEnum]
    runs_inside_refs: list[ARRef]
    sw_addr_method_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ExecutableEntity."""
        super().__init__()
        self.activations: list[ExecutableEntity] = []
        self.can_enter_refs: list[ARRef] = []
        self.exclusive_area_nesting_refs: list[ARRef] = []
        self.minimum_start: Optional[TimeValue] = None
        self.reentrancy_level_enum: Optional[ReentrancyLevelEnum] = None
        self.runs_inside_refs: list[ARRef] = []
        self.sw_addr_method_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ExecutableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activations (list to container "ACTIVATIONS")
        if self.activations:
            wrapper = ET.Element("ACTIVATIONS")
            for item in self.activations:
                serialized = ARObject._serialize_item(item, "ExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_enter_refs (list to container "CAN-ENTER-REFS")
        if self.can_enter_refs:
            wrapper = ET.Element("CAN-ENTER-REFS")
            for item in self.can_enter_refs:
                serialized = ARObject._serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("CAN-ENTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_area_nesting_refs (list to container "EXCLUSIVE-AREA-NESTING-REFS")
        if self.exclusive_area_nesting_refs:
            wrapper = ET.Element("EXCLUSIVE-AREA-NESTING-REFS")
            for item in self.exclusive_area_nesting_refs:
                serialized = ARObject._serialize_item(item, "ExclusiveAreaNestingOrder")
                if serialized is not None:
                    child_elem = ET.Element("EXCLUSIVE-AREA-NESTING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize minimum_start
        if self.minimum_start is not None:
            serialized = ARObject._serialize_item(self.minimum_start, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reentrancy_level_enum
        if self.reentrancy_level_enum is not None:
            serialized = ARObject._serialize_item(self.reentrancy_level_enum, "ReentrancyLevelEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REENTRANCY-LEVEL-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runs_inside_refs (list to container "RUNS-INSIDE-REFS")
        if self.runs_inside_refs:
            wrapper = ET.Element("RUNS-INSIDE-REFS")
            for item in self.runs_inside_refs:
                serialized = ARObject._serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("RUNS-INSIDE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_addr_method_ref
        if self.sw_addr_method_ref is not None:
            serialized = ARObject._serialize_item(self.sw_addr_method_ref, "SwAddrMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ADDR-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntity":
        """Deserialize XML element to ExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutableEntity, cls).deserialize(element)

        # Parse activations (list from container "ACTIVATIONS")
        obj.activations = []
        container = ARObject._find_child_element(element, "ACTIVATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.activations.append(child_value)

        # Parse can_enter_refs (list from container "CAN-ENTER-REFS")
        obj.can_enter_refs = []
        container = ARObject._find_child_element(element, "CAN-ENTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.can_enter_refs.append(child_value)

        # Parse exclusive_area_nesting_refs (list from container "EXCLUSIVE-AREA-NESTING-REFS")
        obj.exclusive_area_nesting_refs = []
        container = ARObject._find_child_element(element, "EXCLUSIVE-AREA-NESTING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_area_nesting_refs.append(child_value)

        # Parse minimum_start
        child = ARObject._find_child_element(element, "MINIMUM-START")
        if child is not None:
            minimum_start_value = child.text
            obj.minimum_start = minimum_start_value

        # Parse reentrancy_level_enum
        child = ARObject._find_child_element(element, "REENTRANCY-LEVEL-ENUM")
        if child is not None:
            reentrancy_level_enum_value = ReentrancyLevelEnum.deserialize(child)
            obj.reentrancy_level_enum = reentrancy_level_enum_value

        # Parse runs_inside_refs (list from container "RUNS-INSIDE-REFS")
        obj.runs_inside_refs = []
        container = ARObject._find_child_element(element, "RUNS-INSIDE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runs_inside_refs.append(child_value)

        # Parse sw_addr_method_ref
        child = ARObject._find_child_element(element, "SW-ADDR-METHOD-REF")
        if child is not None:
            sw_addr_method_ref_value = ARRef.deserialize(child)
            obj.sw_addr_method_ref = sw_addr_method_ref_value

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
