"""FlexrayFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)


class FlexrayFrameTriggering(FrameTriggering):
    """AUTOSAR FlexrayFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    absolutelies: list[FlexrayAbsolutelyScheduledTiming]
    allow_dynamic: Optional[Boolean]
    message_id: Optional[PositiveInteger]
    payload_preamble: Optional[Any]
    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self.absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFrameTriggering":
        """Deserialize XML element to FlexrayFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFrameTriggering object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse absolutelies (list)
        obj.absolutelies = []
        for child in ARObject._find_all_child_elements(element, "ABSOLUTELIES"):
            absolutelies_value = ARObject._deserialize_by_tag(child, "FlexrayAbsolutelyScheduledTiming")
            obj.absolutelies.append(absolutelies_value)

        # Parse allow_dynamic
        child = ARObject._find_child_element(element, "ALLOW-DYNAMIC")
        if child is not None:
            allow_dynamic_value = child.text
            obj.allow_dynamic = allow_dynamic_value

        # Parse message_id
        child = ARObject._find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse payload_preamble
        child = ARObject._find_child_element(element, "PAYLOAD-PREAMBLE")
        if child is not None:
            payload_preamble_value = child.text
            obj.payload_preamble = payload_preamble_value

        return obj



class FlexrayFrameTriggeringBuilder:
    """Builder for FlexrayFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrameTriggering = FlexrayFrameTriggering()

    def build(self) -> FlexrayFrameTriggering:
        """Build and return FlexrayFrameTriggering object.

        Returns:
            FlexrayFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
