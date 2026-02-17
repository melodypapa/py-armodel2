"""TagWithOptionalValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 477)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_TagWithOptionalValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class TagWithOptionalValue(ARObject):
    """AUTOSAR TagWithOptionalValue."""

    key: Optional[String]
    sequence_offset: Optional[Integer]
    value: Optional[String]
    def __init__(self) -> None:
        """Initialize TagWithOptionalValue."""
        super().__init__()
        self.key: Optional[String] = None
        self.sequence_offset: Optional[Integer] = None
        self.value: Optional[String] = None


class TagWithOptionalValueBuilder:
    """Builder for TagWithOptionalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TagWithOptionalValue = TagWithOptionalValue()

    def build(self) -> TagWithOptionalValue:
        """Build and return TagWithOptionalValue object.

        Returns:
            TagWithOptionalValue instance
        """
        # TODO: Add validation
        return self._obj
