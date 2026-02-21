"""SwTextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 249)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)


class SwTextProps(ARObject):
    """AUTOSAR SwTextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size: Optional[ArraySizeSemanticsEnum]
    base_type_ref: Optional[ARRef]
    sw_fill_character: Optional[Integer]
    sw_max_text_size: Optional[Integer]
    def __init__(self) -> None:
        """Initialize SwTextProps."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.base_type_ref: Optional[ARRef] = None
        self.sw_fill_character: Optional[Integer] = None
        self.sw_max_text_size: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize SwTextProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwTextProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size
        if self.array_size is not None:
            serialized = SerializationHelper.serialize_item(self.array_size, "ArraySizeSemanticsEnum")
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

        # Serialize base_type_ref
        if self.base_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_ref, "SwBaseType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_fill_character
        if self.sw_fill_character is not None:
            serialized = SerializationHelper.serialize_item(self.sw_fill_character, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-FILL-CHARACTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_max_text_size
        if self.sw_max_text_size is not None:
            serialized = SerializationHelper.serialize_item(self.sw_max_text_size, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAX-TEXT-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwTextProps":
        """Deserialize XML element to SwTextProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwTextProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwTextProps, cls).deserialize(element)

        # Parse array_size
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = ArraySizeSemanticsEnum.deserialize(child)
            obj.array_size = array_size_value

        # Parse base_type_ref
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-REF")
        if child is not None:
            base_type_ref_value = ARRef.deserialize(child)
            obj.base_type_ref = base_type_ref_value

        # Parse sw_fill_character
        child = SerializationHelper.find_child_element(element, "SW-FILL-CHARACTER")
        if child is not None:
            sw_fill_character_value = child.text
            obj.sw_fill_character = sw_fill_character_value

        # Parse sw_max_text_size
        child = SerializationHelper.find_child_element(element, "SW-MAX-TEXT-SIZE")
        if child is not None:
            sw_max_text_size_value = child.text
            obj.sw_max_text_size = sw_max_text_size_value

        return obj



class SwTextPropsBuilder:
    """Builder for SwTextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwTextProps = SwTextProps()

    def build(self) -> SwTextProps:
        """Build and return SwTextProps object.

        Returns:
            SwTextProps instance
        """
        # TODO: Add validation
        return self._obj
