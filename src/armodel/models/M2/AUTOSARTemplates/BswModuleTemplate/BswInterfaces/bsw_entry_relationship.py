"""BswEntryRelationship AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswEntryRelationship(ARObject):
    """AUTOSAR BswEntryRelationship."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_entry: Optional[BswEntryRelationship]
    from_: Optional[BswModuleEntry]
    to: Optional[BswModuleEntry]
    def __init__(self) -> None:
        """Initialize BswEntryRelationship."""
        super().__init__()
        self.bsw_entry: Optional[BswEntryRelationship] = None
        self.from_: Optional[BswModuleEntry] = None
        self.to: Optional[BswModuleEntry] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationship":
        """Deserialize XML element to BswEntryRelationship object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationship object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_entry
        child = ARObject._find_child_element(element, "BSW-ENTRY")
        if child is not None:
            bsw_entry_value = ARObject._deserialize_by_tag(child, "BswEntryRelationship")
            obj.bsw_entry = bsw_entry_value

        # Parse from_
        child = ARObject._find_child_element(element, "FROM")
        if child is not None:
            from__value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.from_ = from__value

        # Parse to
        child = ARObject._find_child_element(element, "TO")
        if child is not None:
            to_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.to = to_value

        return obj



class BswEntryRelationshipBuilder:
    """Builder for BswEntryRelationship."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationship = BswEntryRelationship()

    def build(self) -> BswEntryRelationship:
        """Build and return BswEntryRelationship object.

        Returns:
            BswEntryRelationship instance
        """
        # TODO: Add validation
        return self._obj
