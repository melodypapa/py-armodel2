"""UnassignFrameId AUTOSAR element.

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


class UnassignFrameId(LinConfigurationEntry):
    """AUTOSAR UnassignFrameId."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    unassigned_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize UnassignFrameId."""
        super().__init__()
        self.unassigned_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnassignFrameId":
        """Deserialize XML element to UnassignFrameId object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UnassignFrameId object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse unassigned_ref
        child = ARObject._find_child_element(element, "UNASSIGNED")
        if child is not None:
            unassigned_ref_value = ARObject._deserialize_by_tag(child, "LinFrameTriggering")
            obj.unassigned_ref = unassigned_ref_value

        return obj



class UnassignFrameIdBuilder:
    """Builder for UnassignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnassignFrameId = UnassignFrameId()

    def build(self) -> UnassignFrameId:
        """Build and return UnassignFrameId object.

        Returns:
            UnassignFrameId instance
        """
        # TODO: Add validation
        return self._obj
