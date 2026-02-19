"""CanFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameRxBehaviorEnum,
    CanFrameTxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_xl_frame_triggering_props import (
    CanXlFrameTriggeringProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_absolutely_scheduled_timing import (
    TtcanAbsolutelyScheduledTiming,
)


class CanFrameTriggering(FrameTriggering):
    """AUTOSAR CanFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    absolutelies: list[TtcanAbsolutelyScheduledTiming]
    can_addressing: Optional[CanAddressingModeType]
    can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_xl_frame_ref: Optional[ARRef]
    identifier: Optional[Integer]
    j1939requestable: Optional[Boolean]
    rx_identifier_range_range: Optional[RxIdentifierRange]
    rx_mask: Optional[PositiveInteger]
    tx_mask: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanFrameTriggering."""
        super().__init__()
        self.absolutelies: list[TtcanAbsolutelyScheduledTiming] = []
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_xl_frame_ref: Optional[ARRef] = None
        self.identifier: Optional[Integer] = None
        self.j1939requestable: Optional[Boolean] = None
        self.rx_identifier_range_range: Optional[RxIdentifierRange] = None
        self.rx_mask: Optional[PositiveInteger] = None
        self.tx_mask: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrameTriggering":
        """Deserialize XML element to CanFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanFrameTriggering, cls).deserialize(element)

        # Parse absolutelies (list from container "ABSOLUTELIES")
        obj.absolutelies = []
        container = ARObject._find_child_element(element, "ABSOLUTELIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.absolutelies.append(child_value)

        # Parse can_addressing
        child = ARObject._find_child_element(element, "CAN-ADDRESSING")
        if child is not None:
            can_addressing_value = CanAddressingModeType.deserialize(child)
            obj.can_addressing = can_addressing_value

        # Parse can_frame_rx_behavior
        child = ARObject._find_child_element(element, "CAN-FRAME-RX-BEHAVIOR")
        if child is not None:
            can_frame_rx_behavior_value = CanFrameRxBehaviorEnum.deserialize(child)
            obj.can_frame_rx_behavior = can_frame_rx_behavior_value

        # Parse can_frame_tx_behavior
        child = ARObject._find_child_element(element, "CAN-FRAME-TX-BEHAVIOR")
        if child is not None:
            can_frame_tx_behavior_value = CanFrameTxBehaviorEnum.deserialize(child)
            obj.can_frame_tx_behavior = can_frame_tx_behavior_value

        # Parse can_xl_frame_ref
        child = ARObject._find_child_element(element, "CAN-XL-FRAME")
        if child is not None:
            can_xl_frame_ref_value = ARObject._deserialize_by_tag(child, "CanXlFrameTriggeringProps")
            obj.can_xl_frame_ref = can_xl_frame_ref_value

        # Parse identifier
        child = ARObject._find_child_element(element, "IDENTIFIER")
        if child is not None:
            identifier_value = child.text
            obj.identifier = identifier_value

        # Parse j1939requestable
        child = ARObject._find_child_element(element, "J1939REQUESTABLE")
        if child is not None:
            j1939requestable_value = child.text
            obj.j1939requestable = j1939requestable_value

        # Parse rx_identifier_range_range
        child = ARObject._find_child_element(element, "RX-IDENTIFIER-RANGE-RANGE")
        if child is not None:
            rx_identifier_range_range_value = ARObject._deserialize_by_tag(child, "RxIdentifierRange")
            obj.rx_identifier_range_range = rx_identifier_range_range_value

        # Parse rx_mask
        child = ARObject._find_child_element(element, "RX-MASK")
        if child is not None:
            rx_mask_value = child.text
            obj.rx_mask = rx_mask_value

        # Parse tx_mask
        child = ARObject._find_child_element(element, "TX-MASK")
        if child is not None:
            tx_mask_value = child.text
            obj.tx_mask = tx_mask_value

        return obj



class CanFrameTriggeringBuilder:
    """Builder for CanFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrameTriggering = CanFrameTriggering()

    def build(self) -> CanFrameTriggering:
        """Build and return CanFrameTriggering object.

        Returns:
            CanFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
