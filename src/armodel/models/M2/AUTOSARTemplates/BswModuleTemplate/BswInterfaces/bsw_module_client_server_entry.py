"""BswModuleClientServerEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "encapsulated": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # encapsulated
        "is_reentrant": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isReentrant
        "is_synchronous": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isSynchronous
    }

    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated: Optional[BswModuleEntry] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None


class BswModuleClientServerEntryBuilder:
    """Builder for BswModuleClientServerEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()

    def build(self) -> BswModuleClientServerEntry:
        """Build and return BswModuleClientServerEntry object.

        Returns:
            BswModuleClientServerEntry instance
        """
        # TODO: Add validation
        return self._obj
