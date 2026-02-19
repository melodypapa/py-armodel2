"""AssignFrameId AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 436)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class AssignFrameId(LinConfigurationEntry):
    """AUTOSAR AssignFrameId."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_frame_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AssignFrameId."""
        super().__init__()
        self.assigned_frame_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssignFrameId":
        """Deserialize XML element to AssignFrameId object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssignFrameId object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AssignFrameId, cls).deserialize(element)

        # Parse assigned_frame_ref
        child = ARObject._find_child_element(element, "ASSIGNED-FRAME")
        if child is not None:
            assigned_frame_ref_value = ARObject._deserialize_by_tag(child, "LinFrameTriggering")
            obj.assigned_frame_ref = assigned_frame_ref_value

        return obj



class AssignFrameIdBuilder:
    """Builder for AssignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameId = AssignFrameId()

    def build(self) -> AssignFrameId:
        """Build and return AssignFrameId object.

        Returns:
            AssignFrameId instance
        """
        # TODO: Add validation
        return self._obj
