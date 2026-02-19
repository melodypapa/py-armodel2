"""ImplementationDataTypeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 269)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2032)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import (
    AbstractImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """AUTOSAR ImplementationDataTypeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_impl_policy_enum: Optional[ArrayImplPolicyEnum]
    array_size: Optional[ArraySizeSemanticsEnum]
    array_size_handling: Optional[ArraySizeHandlingEnum]
    is_optional: Optional[Boolean]
    sub_elements: list[Any]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElement."""
        super().__init__()
        self.array_impl_policy_enum: Optional[ArrayImplPolicyEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.is_optional: Optional[Boolean] = None
        self.sub_elements: list[Any] = []
        self.sw_data_def: Optional[SwDataDefProps] = None
    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_impl_policy_enum
        if self.array_impl_policy_enum is not None:
            serialized = ARObject._serialize_item(self.array_impl_policy_enum, "ArrayImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-IMPL-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size
        if self.array_size is not None:
            serialized = ARObject._serialize_item(self.array_size, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size_handling
        if self.array_size_handling is not None:
            serialized = ARObject._serialize_item(self.array_size_handling, "ArraySizeHandlingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = ARObject._serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = ARObject._serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElement":
        """Deserialize XML element to ImplementationDataTypeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeElement, cls).deserialize(element)

        # Parse array_impl_policy_enum
        child = ARObject._find_child_element(element, "ARRAY-IMPL-POLICY-ENUM")
        if child is not None:
            array_impl_policy_enum_value = ArrayImplPolicyEnum.deserialize(child)
            obj.array_impl_policy_enum = array_impl_policy_enum_value

        # Parse array_size
        child = ARObject._find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = ArraySizeSemanticsEnum.deserialize(child)
            obj.array_size = array_size_value

        # Parse array_size_handling
        child = ARObject._find_child_element(element, "ARRAY-SIZE-HANDLING")
        if child is not None:
            array_size_handling_value = ArraySizeHandlingEnum.deserialize(child)
            obj.array_size_handling = array_size_handling_value

        # Parse is_optional
        child = ARObject._find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = ARObject._find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class ImplementationDataTypeElementBuilder:
    """Builder for ImplementationDataTypeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeElement = ImplementationDataTypeElement()

    def build(self) -> ImplementationDataTypeElement:
        """Build and return ImplementationDataTypeElement object.

        Returns:
            ImplementationDataTypeElement instance
        """
        # TODO: Add validation
        return self._obj
