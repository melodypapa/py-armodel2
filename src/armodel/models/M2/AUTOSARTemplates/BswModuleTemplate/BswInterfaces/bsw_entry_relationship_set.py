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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEntryRelationshipSet, cls).deserialize(element)

        # Parse bsw_entry_relationships (list from container "BSW-ENTRY-RELATIONSHIPS")
        obj.bsw_entry_relationships = []
        container = ARObject._find_child_element(element, "BSW-ENTRY-RELATIONSHIPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_entry_relationships.append(child_value)

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
