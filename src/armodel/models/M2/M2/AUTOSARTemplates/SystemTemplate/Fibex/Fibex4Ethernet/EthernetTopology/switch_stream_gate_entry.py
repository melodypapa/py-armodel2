"""SwitchStreamGateEntry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "internal_priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # internalPriority
    }

    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None


class SwitchStreamGateEntryBuilder:
    """Builder for SwitchStreamGateEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()

    def build(self) -> SwitchStreamGateEntry:
        """Build and return SwitchStreamGateEntry object.

        Returns:
            SwitchStreamGateEntry instance
        """
        # TODO: Add validation
        return self._obj
