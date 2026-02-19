"""ImplementationDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 230)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 268)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2031)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 47)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 451)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 193)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.implementation_data_type_element import (
    ImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)


class ImplementationDataType(AbstractImplementationDataType):
    """AUTOSAR ImplementationDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_array_size_profile: Optional[String]
    is_struct_with_optional_element: Optional[Boolean]
    sub_elements: list[ImplementationDataTypeElement]
    symbol_props: Optional[SymbolProps]
    type_emitter: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize ImplementationDataType."""
        super().__init__()
        self.dynamic_array_size_profile: Optional[String] = None
        self.is_struct_with_optional_element: Optional[Boolean] = None
        self.sub_elements: list[ImplementationDataTypeElement] = []
        self.symbol_props: Optional[SymbolProps] = None
        self.type_emitter: Optional[NameToken] = None
    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_array_size_profile
        if self.dynamic_array_size_profile is not None:
            serialized = ARObject._serialize_item(self.dynamic_array_size_profile, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-ARRAY-SIZE-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_struct_with_optional_element
        if self.is_struct_with_optional_element is not None:
            serialized = ARObject._serialize_item(self.is_struct_with_optional_element, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-STRUCT-WITH-OPTIONAL-ELEMENT")
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
                serialized = ARObject._serialize_item(item, "ImplementationDataTypeElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol_props
        if self.symbol_props is not None:
            serialized = ARObject._serialize_item(self.symbol_props, "SymbolProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_emitter
        if self.type_emitter is not None:
            serialized = ARObject._serialize_item(self.type_emitter, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-EMITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataType":
        """Deserialize XML element to ImplementationDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataType, cls).deserialize(element)

        # Parse dynamic_array_size_profile
        child = ARObject._find_child_element(element, "DYNAMIC-ARRAY-SIZE-PROFILE")
        if child is not None:
            dynamic_array_size_profile_value = child.text
            obj.dynamic_array_size_profile = dynamic_array_size_profile_value

        # Parse is_struct_with_optional_element
        child = ARObject._find_child_element(element, "IS-STRUCT-WITH-OPTIONAL-ELEMENT")
        if child is not None:
            is_struct_with_optional_element_value = child.text
            obj.is_struct_with_optional_element = is_struct_with_optional_element_value

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = ARObject._find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

        # Parse symbol_props
        child = ARObject._find_child_element(element, "SYMBOL-PROPS")
        if child is not None:
            symbol_props_value = ARObject._deserialize_by_tag(child, "SymbolProps")
            obj.symbol_props = symbol_props_value

        # Parse type_emitter
        child = ARObject._find_child_element(element, "TYPE-EMITTER")
        if child is not None:
            type_emitter_value = child.text
            obj.type_emitter = type_emitter_value

        return obj



class ImplementationDataTypeBuilder:
    """Builder for ImplementationDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataType = ImplementationDataType()

    def build(self) -> ImplementationDataType:
        """Build and return ImplementationDataType object.

        Returns:
            ImplementationDataType instance
        """
        # TODO: Add validation
        return self._obj
