"""NvBlockDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDataMapping":
        """Deserialize XML element to NvBlockDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockDataMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bitfield_text_table
        child = ARObject._find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse nv_ram_block_ref
        child = ARObject._find_child_element(element, "NV-RAM-BLOCK")
        if child is not None:
            nv_ram_block_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.nv_ram_block_ref = nv_ram_block_ref_value

        # Parse read_nv_data_ref
        child = ARObject._find_child_element(element, "READ-NV-DATA")
        if child is not None:
            read_nv_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.read_nv_data_ref = read_nv_data_ref_value

        # Parse written_nv_data_ref
        child = ARObject._find_child_element(element, "WRITTEN-NV-DATA")
        if child is not None:
            written_nv_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.written_nv_data_ref = written_nv_data_ref_value

        # Parse written_read_nv_ref
        child = ARObject._find_child_element(element, "WRITTEN-READ-NV")
        if child is not None:
            written_read_nv_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
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
