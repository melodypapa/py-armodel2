"""BswEntryRelationship AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswEntryRelationship(ARObject):
    """AUTOSAR BswEntryRelationship."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswEntryRelationship,
        ),  # bswEntry
        "from_": XMLMember(
            xml_tag='FROM',
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
            xml_name_override='FROM',
        ),  # from
        "to": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # to
    }

    def __init__(self) -> None:
        """Initialize BswEntryRelationship."""
        super().__init__()
        self.bsw_entry: Optional[BswEntryRelationship] = None
        self.from_: Optional[BswModuleEntry] = None
        self.to: Optional[BswModuleEntry] = None


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
