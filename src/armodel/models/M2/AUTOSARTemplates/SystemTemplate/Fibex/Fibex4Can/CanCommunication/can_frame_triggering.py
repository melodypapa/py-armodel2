"""CanFrameTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("absolutelies", None, False, True, TtcanAbsolutelyScheduledTiming),  # absolutelies
        ("can_addressing", None, False, False, CanAddressingModeType),  # canAddressing
        ("can_frame_rx_behavior", None, False, False, CanFrameRxBehaviorEnum),  # canFrameRxBehavior
        ("can_frame_tx_behavior", None, False, False, CanFrameTxBehaviorEnum),  # canFrameTxBehavior
        ("can_xl_frame", None, False, False, CanXlFrameTriggeringProps),  # canXlFrame
        ("identifier", None, True, False, None),  # identifier
        ("j1939requestable", None, True, False, None),  # j1939requestable
        ("rx_identifier_range_range", None, False, False, RxIdentifierRange),  # rxIdentifierRangeRange
        ("rx_mask", None, True, False, None),  # rxMask
        ("tx_mask", None, True, False, None),  # txMask
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanFrameTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrameTriggering":
        """Create CanFrameTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanFrameTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanFrameTriggering since parent returns ARObject
        return cast("CanFrameTriggering", obj)


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
