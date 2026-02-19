"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MappingDirectionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    identical: Optional[Boolean]
    mapping_ref: Optional[ARRef]
    value_pairs: list[TextTableValuePair]
    def __init__(self) -> None:
        """Initialize TextTableMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.identical: Optional[Boolean] = None
        self.mapping_ref: Optional[ARRef] = None
        self.value_pairs: list[TextTableValuePair] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableMapping":
        """Deserialize XML element to TextTableMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bitfield_text_table
        child = ARObject._find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse identical
        child = ARObject._find_child_element(element, "IDENTICAL")
        if child is not None:
            identical_value = child.text
            obj.identical = identical_value

        # Parse mapping_ref
        child = ARObject._find_child_element(element, "MAPPING")
        if child is not None:
            mapping_ref_value = child.text
            obj.mapping_ref = mapping_ref_value

        # Parse value_pairs (list)
        obj.value_pairs = []
        for child in ARObject._find_all_child_elements(element, "VALUE-PAIRS"):
            value_pairs_value = ARObject._deserialize_by_tag(child, "TextTableValuePair")
            obj.value_pairs.append(value_pairs_value)

        return obj



class TextTableMappingBuilder:
    """Builder for TextTableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableMapping = TextTableMapping()

    def build(self) -> TextTableMapping:
        """Build and return TextTableMapping object.

        Returns:
            TextTableMapping instance
        """
        # TODO: Add validation
        return self._obj
