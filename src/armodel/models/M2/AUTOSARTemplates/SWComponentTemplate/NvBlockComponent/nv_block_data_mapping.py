"""NvBlockDataMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class NvBlockDataMapping(ARObject):
    """AUTOSAR NvBlockDataMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bitfield_text_table": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bitfieldTextTable
        "nv_ram_block": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # nvRamBlock
        "read_nv_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # readNvData
        "written_nv_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # writtenNvData
        "written_read_nv": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # writtenReadNv
    }

    def __init__(self) -> None:
        """Initialize NvBlockDataMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.nv_ram_block: Optional[AutosarVariableRef] = None
        self.read_nv_data: Optional[AutosarVariableRef] = None
        self.written_nv_data: Optional[AutosarVariableRef] = None
        self.written_read_nv: Optional[AutosarVariableRef] = None


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
