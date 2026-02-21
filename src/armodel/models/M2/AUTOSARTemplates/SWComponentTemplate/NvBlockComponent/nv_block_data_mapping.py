"""NvBlockDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class NvBlockDataMapping(ARObject):
    """AUTOSAR NvBlockDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    nv_ram_block_ref: Optional[ARRef]
    read_nv_data_ref: Optional[ARRef]
    written_nv_data_ref: Optional[ARRef]
    written_read_nv_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvBlockDataMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.nv_ram_block_ref: Optional[ARRef] = None
        self.read_nv_data_ref: Optional[ARRef] = None
        self.written_nv_data_ref: Optional[ARRef] = None
        self.written_read_nv_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize NvBlockDataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockDataMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bitfield_text_table
        if self.bitfield_text_table is not None:
            serialized = SerializationHelper.serialize_item(self.bitfield_text_table, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BITFIELD-TEXT-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nv_ram_block_ref
        if self.nv_ram_block_ref is not None:
            serialized = SerializationHelper.serialize_item(self.nv_ram_block_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NV-RAM-BLOCK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize read_nv_data_ref
        if self.read_nv_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.read_nv_data_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-NV-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize written_nv_data_ref
        if self.written_nv_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.written_nv_data_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITTEN-NV-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize written_read_nv_ref
        if self.written_read_nv_ref is not None:
            serialized = SerializationHelper.serialize_item(self.written_read_nv_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITTEN-READ-NV-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDataMapping":
        """Deserialize XML element to NvBlockDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockDataMapping, cls).deserialize(element)

        # Parse bitfield_text_table
        child = SerializationHelper.find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse nv_ram_block_ref
        child = SerializationHelper.find_child_element(element, "NV-RAM-BLOCK-REF")
        if child is not None:
            nv_ram_block_ref_value = ARRef.deserialize(child)
            obj.nv_ram_block_ref = nv_ram_block_ref_value

        # Parse read_nv_data_ref
        child = SerializationHelper.find_child_element(element, "READ-NV-DATA-REF")
        if child is not None:
            read_nv_data_ref_value = ARRef.deserialize(child)
            obj.read_nv_data_ref = read_nv_data_ref_value

        # Parse written_nv_data_ref
        child = SerializationHelper.find_child_element(element, "WRITTEN-NV-DATA-REF")
        if child is not None:
            written_nv_data_ref_value = ARRef.deserialize(child)
            obj.written_nv_data_ref = written_nv_data_ref_value

        # Parse written_read_nv_ref
        child = SerializationHelper.find_child_element(element, "WRITTEN-READ-NV-REF")
        if child is not None:
            written_read_nv_ref_value = ARRef.deserialize(child)
            obj.written_read_nv_ref = written_read_nv_ref_value

        return obj



class NvBlockDataMappingBuilder:
    """Builder for NvBlockDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockDataMapping = NvBlockDataMapping()

    def build(self) -> NvBlockDataMapping:
        """Build and return NvBlockDataMapping object.

        Returns:
            NvBlockDataMapping instance
        """
        # TODO: Add validation
        return self._obj
