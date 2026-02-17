"""TDEventBswModule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_module_entry_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # bswModuleEntryEntry
        "td_event_bsw": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventBswModule,
        ),  # tdEventBsw
    }

    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry: Optional[BswModuleEntry] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None


class TDEventBswModuleBuilder:
    """Builder for TDEventBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModule = TDEventBswModule()

    def build(self) -> TDEventBswModule:
        """Build and return TDEventBswModule object.

        Returns:
            TDEventBswModule instance
        """
        # TODO: Add validation
        return self._obj
