"""TtcanAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 450)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import (
    TtcanTriggerType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class TtcanAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR TtcanAbsolutelyScheduledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_cycle_cycle: Optional[CommunicationCycle]
    time_mark: Optional[Integer]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TtcanAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.time_mark: Optional[Integer] = None
        self.trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanAbsolutelyScheduledTiming":
        """Deserialize XML element to TtcanAbsolutelyScheduledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanAbsolutelyScheduledTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_cycle_cycle
        child = ARObject._find_child_element(element, "COMMUNICATION-CYCLE-CYCLE")
        if child is not None:
            communication_cycle_cycle_value = ARObject._deserialize_by_tag(child, "CommunicationCycle")
            obj.communication_cycle_cycle = communication_cycle_cycle_value

        # Parse time_mark
        child = ARObject._find_child_element(element, "TIME-MARK")
        if child is not None:
            time_mark_value = child.text
            obj.time_mark = time_mark_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = child.text
            obj.trigger_ref = trigger_ref_value

        return obj



class TtcanAbsolutelyScheduledTimingBuilder:
    """Builder for TtcanAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanAbsolutelyScheduledTiming = TtcanAbsolutelyScheduledTiming()

    def build(self) -> TtcanAbsolutelyScheduledTiming:
        """Build and return TtcanAbsolutelyScheduledTiming object.

        Returns:
            TtcanAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
