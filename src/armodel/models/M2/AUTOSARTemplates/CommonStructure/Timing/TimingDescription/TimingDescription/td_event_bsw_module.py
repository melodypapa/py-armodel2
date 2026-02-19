"""TDEventBswModule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_entry_entry: Optional[BswModuleEntry]
    td_event_bsw: Optional[TDEventBswModule]
    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry: Optional[BswModuleEntry] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModule":
        """Deserialize XML element to TDEventBswModule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswModule object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_module_entry_entry
        child = ARObject._find_child_element(element, "BSW-MODULE-ENTRY-ENTRY")
        if child is not None:
            bsw_module_entry_entry_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.bsw_module_entry_entry = bsw_module_entry_entry_value

        # Parse td_event_bsw
        child = ARObject._find_child_element(element, "TD-EVENT-BSW")
        if child is not None:
            td_event_bsw_value = ARObject._deserialize_by_tag(child, "TDEventBswModule")
            obj.td_event_bsw = td_event_bsw_value

        return obj



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
