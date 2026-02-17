"""DataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 981)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class DataMapping(ARObject):
    """AUTOSAR DataMapping."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DataMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None


class DataMappingBuilder:
    """Builder for DataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataMapping = DataMapping()

    def build(self) -> DataMapping:
        """Build and return DataMapping object.

        Returns:
            DataMapping instance
        """
        # TODO: Add validation
        return self._obj
