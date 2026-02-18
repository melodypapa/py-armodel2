"""EnumerationMappingTable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class EnumerationMappingTable(PackageableElement):
    """AUTOSAR EnumerationMappingTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entrie_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EnumerationMappingTable."""
        super().__init__()
        self.entrie_refs: list[ARRef] = []


class EnumerationMappingTableBuilder:
    """Builder for EnumerationMappingTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingTable = EnumerationMappingTable()

    def build(self) -> EnumerationMappingTable:
        """Build and return EnumerationMappingTable object.

        Returns:
            EnumerationMappingTable instance
        """
        # TODO: Add validation
        return self._obj
