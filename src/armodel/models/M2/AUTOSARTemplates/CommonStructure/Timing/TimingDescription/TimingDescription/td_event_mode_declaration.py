"""TDEventModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class TDEventModeDeclaration(TDEventVfbPort):
    """AUTOSAR TDEventModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entry_mode: Optional[ModeDeclaration]
    exit_mode: Optional[ModeDeclaration]
    mode_ref: Optional[ARRef]
    td_event_mode: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventModeDeclaration."""
        super().__init__()
        self.entry_mode: Optional[ModeDeclaration] = None
        self.exit_mode: Optional[ModeDeclaration] = None
        self.mode_ref: Optional[ARRef] = None
        self.td_event_mode: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventModeDeclaration":
        """Deserialize XML element to TDEventModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventModeDeclaration, cls).deserialize(element)

        # Parse entry_mode
        child = ARObject._find_child_element(element, "ENTRY-MODE")
        if child is not None:
            entry_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.entry_mode = entry_mode_value

        # Parse exit_mode
        child = ARObject._find_child_element(element, "EXIT-MODE")
        if child is not None:
            exit_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.exit_mode = exit_mode_value

        # Parse mode_ref
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_ref = mode_ref_value

        # Parse td_event_mode
        child = ARObject._find_child_element(element, "TD-EVENT-MODE")
        if child is not None:
            td_event_mode_value = child.text
            obj.td_event_mode = td_event_mode_value

        return obj



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
