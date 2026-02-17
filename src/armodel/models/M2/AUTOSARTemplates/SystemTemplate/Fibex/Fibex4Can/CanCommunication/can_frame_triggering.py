"""CanFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "absolutelies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TtcanAbsolutelyScheduledTiming,
        ),  # absolutelies
        "can_addressing": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanAddressingModeType,
        ),  # canAddressing
        "can_frame_rx_behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanFrameRxBehaviorEnum,
        ),  # canFrameRxBehavior
        "can_frame_tx_behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanFrameTxBehaviorEnum,
        ),  # canFrameTxBehavior
        "can_xl_frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanXlFrameTriggeringProps,
        ),  # canXlFrame
        "identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # identifier
        "j1939requestable": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # j1939requestable
        "rx_identifier_range_range": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RxIdentifierRange,
        ),  # rxIdentifierRangeRange
        "rx_mask": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rxMask
        "tx_mask": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # txMask
    }

    def __init__(self) -> None:
        """Initialize CanFrameTriggering."""
        super().__init__()
        self.absolutelies: list[TtcanAbsolutelyScheduledTiming] = []
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_xl_frame: Optional[CanXlFrameTriggeringProps] = None
        self.identifier: Optional[Integer] = None
        self.j1939requestable: Optional[Boolean] = None
        self.rx_identifier_range_range: Optional[RxIdentifierRange] = None
        self.rx_mask: Optional[PositiveInteger] = None
        self.tx_mask: Optional[PositiveInteger] = None


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
