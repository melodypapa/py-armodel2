"""InternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 319)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 516)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 231)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 453)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod


class InternalBehavior(Identifiable, ABC):
    """AUTOSAR InternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    constants: list[ParameterDataPrototype]
    constant_value_refs: list[ARRef]
    data_type_refs: list[ARRef]
    exclusive_areas: list[ExclusiveArea]
    exclusive_area_nestings: list[ExclusiveAreaNestingOrder]
    static_memorie_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constants: list[ParameterDataPrototype] = []
        self.constant_value_refs: list[ARRef] = []
        self.data_type_refs: list[ARRef] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.static_memorie_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize InternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constants (list to container "CONSTANTS")
        if self.constants:
            wrapper = ET.Element("CONSTANTS")
            for item in self.constants:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constant_value_refs (list to container "CONSTANT-VALUE-REFS")
        if self.constant_value_refs:
            wrapper = ET.Element("CONSTANT-VALUE-REFS")
            for item in self.constant_value_refs:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecification")
                if serialized is not None:
                    child_elem = ET.Element("CONSTANT-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_refs (list to container "DATA-TYPE-REFS")
        if self.data_type_refs:
            wrapper = ET.Element("DATA-TYPE-REFS")
            for item in self.data_type_refs:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_areas (list to container "EXCLUSIVE-AREAS")
        if self.exclusive_areas:
            wrapper = ET.Element("EXCLUSIVE-AREAS")
            for item in self.exclusive_areas:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_area_nestings (list to container "EXCLUSIVE-AREA-NESTINGS")
        if self.exclusive_area_nestings:
            wrapper = ET.Element("EXCLUSIVE-AREA-NESTINGS")
            for item in self.exclusive_area_nestings:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveAreaNestingOrder")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize static_memorie_refs (list to container "STATIC-MEMORIE-REFS")
        if self.static_memorie_refs:
            wrapper = ET.Element("STATIC-MEMORIE-REFS")
            for item in self.static_memorie_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("STATIC-MEMORIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalBehavior":
        """Deserialize XML element to InternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InternalBehavior, cls).deserialize(element)

        # Parse constants (list from container "CONSTANTS")
        obj.constants = []
        container = SerializationHelper.find_child_element(element, "CONSTANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constants.append(child_value)

        # Parse constant_value_refs (list from container "CONSTANT-VALUE-REFS")
        obj.constant_value_refs = []
        container = SerializationHelper.find_child_element(element, "CONSTANT-VALUE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constant_value_refs.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPE-REFS")
        obj.data_type_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-TYPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_refs.append(child_value)

        # Parse exclusive_areas (list from container "EXCLUSIVE-AREAS")
        obj.exclusive_areas = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_areas.append(child_value)

        # Parse exclusive_area_nestings (list from container "EXCLUSIVE-AREA-NESTINGS")
        obj.exclusive_area_nestings = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-NESTINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_area_nestings.append(child_value)

        # Parse static_memorie_refs (list from container "STATIC-MEMORIE-REFS")
        obj.static_memorie_refs = []
        container = SerializationHelper.find_child_element(element, "STATIC-MEMORIE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.static_memorie_refs.append(child_value)

        return obj



