"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bitfield_text_table": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bitfieldTextTable
        "identical": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # identical
        "mapping": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MappingDirectionEnum,
        ),  # mapping
        "value_pairs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TextTableValuePair,
        ),  # valuePairs
    }

    def __init__(self) -> None:
        """Initialize TextTableMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.identical: Optional[Boolean] = None
        self.mapping: Optional[MappingDirectionEnum] = None
        self.value_pairs: list[TextTableValuePair] = []


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
