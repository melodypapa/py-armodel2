"""NvBlockDataMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bitfield_text_table", None, True, False, None),  # bitfieldTextTable
        ("nv_ram_block", None, False, False, AutosarVariableRef),  # nvRamBlock
        ("read_nv_data", None, False, False, AutosarVariableRef),  # readNvData
        ("written_nv_data", None, False, False, AutosarVariableRef),  # writtenNvData
        ("written_read_nv", None, False, False, AutosarVariableRef),  # writtenReadNv
    ]

    def __init__(self) -> None:
        """Initialize NvBlockDataMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.nv_ram_block: Optional[AutosarVariableRef] = None
        self.read_nv_data: Optional[AutosarVariableRef] = None
        self.written_nv_data: Optional[AutosarVariableRef] = None
        self.written_read_nv: Optional[AutosarVariableRef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvBlockDataMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDataMapping":
        """Create NvBlockDataMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvBlockDataMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvBlockDataMapping since parent returns ARObject
        return cast("NvBlockDataMapping", obj)


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
