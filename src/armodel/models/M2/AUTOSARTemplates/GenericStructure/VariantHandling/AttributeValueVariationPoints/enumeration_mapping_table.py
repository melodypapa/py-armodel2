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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingTable":
        """Deserialize XML element to EnumerationMappingTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EnumerationMappingTable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse entrie_refs (list)
        obj.entrie_refs = []
        for child in ARObject._find_all_child_elements(element, "ENTRIES"):
            entrie_refs_value = child.text
            obj.entrie_refs.append(entrie_refs_value)

        return obj



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
