"""IndexedArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class IndexedArrayElement(ARObject):
    """AUTOSAR IndexedArrayElement."""

    def __init__(self) -> None:
        """Initialize IndexedArrayElement."""
        super().__init__()
        self.application_array: Optional[Any] = None
        self.implementation: Optional[Any] = None
        self.index: Optional[Integer] = None


class IndexedArrayElementBuilder:
    """Builder for IndexedArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexedArrayElement = IndexedArrayElement()

    def build(self) -> IndexedArrayElement:
        """Build and return IndexedArrayElement object.

        Returns:
            IndexedArrayElement instance
        """
        # TODO: Add validation
        return self._obj
