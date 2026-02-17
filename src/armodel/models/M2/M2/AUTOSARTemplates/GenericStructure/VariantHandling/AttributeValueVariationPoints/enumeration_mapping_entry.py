"""EnumerationMappingEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EnumerationMappingEntry(ARObject):
    """AUTOSAR EnumerationMappingEntry."""

    def __init__(self) -> None:
        """Initialize EnumerationMappingEntry."""
        super().__init__()
        self.enumerator: NameToken = None
        self.numerical_value: PositiveInteger = None


class EnumerationMappingEntryBuilder:
    """Builder for EnumerationMappingEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingEntry = EnumerationMappingEntry()

    def build(self) -> EnumerationMappingEntry:
        """Build and return EnumerationMappingEntry object.

        Returns:
            EnumerationMappingEntry instance
        """
        # TODO: Add validation
        return self._obj
