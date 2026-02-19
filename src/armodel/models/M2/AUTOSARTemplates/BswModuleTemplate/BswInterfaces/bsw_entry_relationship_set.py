"""BswEntryRelationshipSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)


class BswEntryRelationshipSet(ARElement):
    """AUTOSAR BswEntryRelationshipSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_entry_relationships: list[BswEntryRelationship]
    def __init__(self) -> None:
        """Initialize BswEntryRelationshipSet."""
        super().__init__()
        self.bsw_entry_relationships: list[BswEntryRelationship] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationshipSet":
        """Deserialize XML element to BswEntryRelationshipSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationshipSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_entry_relationships (list)
        obj.bsw_entry_relationships = []
        for child in ARObject._find_all_child_elements(element, "BSW-ENTRY-RELATIONSHIPS"):
            bsw_entry_relationships_value = ARObject._deserialize_by_tag(child, "BswEntryRelationship")
            obj.bsw_entry_relationships.append(bsw_entry_relationships_value)

        return obj



class BswEntryRelationshipSetBuilder:
    """Builder for BswEntryRelationshipSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationshipSet = BswEntryRelationshipSet()

    def build(self) -> BswEntryRelationshipSet:
        """Build and return BswEntryRelationshipSet object.

        Returns:
            BswEntryRelationshipSet instance
        """
        # TODO: Add validation
        return self._obj
