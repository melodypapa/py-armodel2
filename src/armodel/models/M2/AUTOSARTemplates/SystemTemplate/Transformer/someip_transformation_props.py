"""SOMEIPTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 783)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationProps(TransformationProps):
    """AUTOSAR SOMEIPTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[PositiveInteger]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationProps."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SOMEIPTransformationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SOMEIPTransformationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_array
        if self.size_of_array is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_array, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-ARRAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_string
        if self.size_of_string is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_string, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_struct
        if self.size_of_struct is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_struct, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-STRUCT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size_of_union
        if self.size_of_union is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_union, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE-OF-UNION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationProps":
        """Deserialize XML element to SOMEIPTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SOMEIPTransformationProps, cls).deserialize(element)

        # Parse alignment
        child = SerializationHelper.find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse size_of_array
        child = SerializationHelper.find_child_element(element, "SIZE-OF-ARRAY")
        if child is not None:
            size_of_array_value = child.text
            obj.size_of_array = size_of_array_value

        # Parse size_of_string
        child = SerializationHelper.find_child_element(element, "SIZE-OF-STRING")
        if child is not None:
            size_of_string_value = child.text
            obj.size_of_string = size_of_string_value

        # Parse size_of_struct
        child = SerializationHelper.find_child_element(element, "SIZE-OF-STRUCT")
        if child is not None:
            size_of_struct_value = child.text
            obj.size_of_struct = size_of_struct_value

        # Parse size_of_union
        child = SerializationHelper.find_child_element(element, "SIZE-OF-UNION")
        if child is not None:
            size_of_union_value = child.text
            obj.size_of_union = size_of_union_value

        return obj



class SOMEIPTransformationPropsBuilder:
    """Builder for SOMEIPTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationProps = SOMEIPTransformationProps()

    def build(self) -> SOMEIPTransformationProps:
        """Build and return SOMEIPTransformationProps object.

        Returns:
            SOMEIPTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
