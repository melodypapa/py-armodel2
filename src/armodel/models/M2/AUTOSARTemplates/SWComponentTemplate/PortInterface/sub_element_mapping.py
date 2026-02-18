"""SubElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SubElementMapping(ARObject):
    """AUTOSAR SubElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_element: Optional[SubElementRef]
    second_element: Optional[SubElementRef]
    text_table: TextTableMapping
    def __init__(self) -> None:
        """Initialize SubElementMapping."""
        super().__init__()
        self.first_element: Optional[SubElementRef] = None
        self.second_element: Optional[SubElementRef] = None
        self.text_table: TextTableMapping = None


class SubElementMappingBuilder:
    """Builder for SubElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementMapping = SubElementMapping()

    def build(self) -> SubElementMapping:
        """Build and return SubElementMapping object.

        Returns:
            SubElementMapping instance
        """
        # TODO: Add validation
        return self._obj
