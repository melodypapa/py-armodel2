"""ApplicationEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class ApplicationEntry(ScheduleTableEntry):
    """AUTOSAR ApplicationEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame_triggering_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ApplicationEntry."""
        super().__init__()
        self.frame_triggering_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationEntry":
        """Deserialize XML element to ApplicationEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationEntry, cls).deserialize(element)

        # Parse frame_triggering_ref
        child = ARObject._find_child_element(element, "FRAME-TRIGGERING")
        if child is not None:
            frame_triggering_ref_value = ARObject._deserialize_by_tag(child, "LinFrameTriggering")
            obj.frame_triggering_ref = frame_triggering_ref_value

        return obj



class ApplicationEntryBuilder:
    """Builder for ApplicationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationEntry = ApplicationEntry()

    def build(self) -> ApplicationEntry:
        """Build and return ApplicationEntry object.

        Returns:
            ApplicationEntry instance
        """
        # TODO: Add validation
        return self._obj
