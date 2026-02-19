"""AssignFrameIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.frame_pid import (
    FramePid,
)


class AssignFrameIdRange(LinConfigurationEntry):
    """AUTOSAR AssignFrameIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame_pid: FramePid
    start_index: Optional[Integer]
    def __init__(self) -> None:
        """Initialize AssignFrameIdRange."""
        super().__init__()
        self.frame_pid: FramePid = None
        self.start_index: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssignFrameIdRange":
        """Deserialize XML element to AssignFrameIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssignFrameIdRange object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse frame_pid
        child = ARObject._find_child_element(element, "FRAME-PID")
        if child is not None:
            frame_pid_value = ARObject._deserialize_by_tag(child, "FramePid")
            obj.frame_pid = frame_pid_value

        # Parse start_index
        child = ARObject._find_child_element(element, "START-INDEX")
        if child is not None:
            start_index_value = child.text
            obj.start_index = start_index_value

        return obj



class AssignFrameIdRangeBuilder:
    """Builder for AssignFrameIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameIdRange = AssignFrameIdRange()

    def build(self) -> AssignFrameIdRange:
        """Build and return AssignFrameIdRange object.

        Returns:
            AssignFrameIdRange instance
        """
        # TODO: Add validation
        return self._obj
