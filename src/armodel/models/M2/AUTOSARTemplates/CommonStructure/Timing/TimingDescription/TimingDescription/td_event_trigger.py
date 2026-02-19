"""TDEventTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventTriggerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TDEventTrigger(TDEventVfbPort):
    """AUTOSAR TDEventTrigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    td_event_trigger_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventTrigger."""
        super().__init__()
        self.td_event_trigger_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventTrigger":
        """Deserialize XML element to TDEventTrigger object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventTrigger object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventTrigger, cls).deserialize(element)

        # Parse td_event_trigger_ref
        child = ARObject._find_child_element(element, "TD-EVENT-TRIGGER")
        if child is not None:
            td_event_trigger_ref_value = TDEventTriggerTypeEnum.deserialize(child)
            obj.td_event_trigger_ref = td_event_trigger_ref_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class TDEventTriggerBuilder:
    """Builder for TDEventTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTrigger = TDEventTrigger()

    def build(self) -> TDEventTrigger:
        """Build and return TDEventTrigger object.

        Returns:
            TDEventTrigger instance
        """
        # TODO: Add validation
        return self._obj
