"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    mapping: Optional[MappingDirectionEnum]
    value_pairs: list[TextTableValuePair]
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
