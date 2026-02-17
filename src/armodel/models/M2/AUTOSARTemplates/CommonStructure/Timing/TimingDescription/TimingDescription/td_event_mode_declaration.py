"""TDEventModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class TDEventModeDeclaration(TDEventVfbPort):
    """AUTOSAR TDEventModeDeclaration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "entry_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # entryMode
        "exit_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # exitMode
        "mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # mode
        "td_event_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (TDEventMode),
        ),  # tdEventMode
    }

    def __init__(self) -> None:
        """Initialize TDEventModeDeclaration."""
        super().__init__()
        self.entry_mode: Optional[ModeDeclaration] = None
        self.exit_mode: Optional[ModeDeclaration] = None
        self.mode: Optional[ModeDeclarationGroup] = None
        self.td_event_mode: Optional[Any] = None


class TDEventModeDeclarationBuilder:
    """Builder for TDEventModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventModeDeclaration = TDEventModeDeclaration()

    def build(self) -> TDEventModeDeclaration:
        """Build and return TDEventModeDeclaration object.

        Returns:
            TDEventModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
