"""FlexrayCommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)


class FlexrayCommunicationController(ARObject):
    """AUTOSAR FlexrayCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accepted", None, True, False, None),  # accepted
        ("allow_halt_due_to", None, True, False, None),  # allowHaltDueTo
        ("allow_passive_to", None, True, False, None),  # allowPassiveTo
        ("cluster_drift", None, True, False, None),  # clusterDrift
        ("decoding", None, True, False, None),  # decoding
        ("delay", None, True, False, None),  # delay
        ("external_sync", None, True, False, None),  # externalSync
        ("extern_offset", None, True, False, None),  # externOffset
        ("extern_rate", None, True, False, None),  # externRate
        ("fall_back_internal", None, True, False, None),  # fallBackInternal
        ("flexray_fifos", None, False, True, any (FlexrayFifo)),  # flexrayFifos
        ("key_slot_id", None, True, False, None),  # keySlotID
        ("key_slot_only", None, True, False, None),  # keySlotOnly
        ("key_slot_used_for", None, True, False, None),  # keySlotUsedFor
        ("latest_tx", None, True, False, None),  # latestTX
        ("listen_timeout", None, True, False, None),  # listenTimeout
        ("macro_initial", None, True, False, None),  # macroInitial
        ("maximum", None, True, False, None),  # maximum
        ("micro_initial", None, True, False, None),  # microInitial
        ("micro_per_cycle", None, True, False, None),  # microPerCycle
        ("microtick", None, True, False, None),  # microtick
        ("nm_vector_early", None, True, False, None),  # nmVectorEarly
        ("offset_correction", None, True, False, None),  # offsetCorrection
        ("rate_correction", None, True, False, None),  # rateCorrection
        ("samples_per_microtick", None, True, False, None),  # samplesPerMicrotick
        ("second_key_slot", None, True, False, None),  # secondKeySlot
        ("two_key_slot", None, True, False, None),  # twoKeySlot
        ("wake_up_pattern", None, True, False, None),  # wakeUpPattern
    ]

    def __init__(self) -> None:
        """Initialize FlexrayCommunicationController."""
        super().__init__()
        self.accepted: Optional[Integer] = None
        self.allow_halt_due_to: Optional[Boolean] = None
        self.allow_passive_to: Optional[Integer] = None
        self.cluster_drift: Optional[Integer] = None
        self.decoding: Optional[Integer] = None
        self.delay: Optional[Integer] = None
        self.external_sync: Optional[Boolean] = None
        self.extern_offset: Optional[Integer] = None
        self.extern_rate: Optional[Integer] = None
        self.fall_back_internal: Optional[Boolean] = None
        self.flexray_fifos: list[Any] = []
        self.key_slot_id: Optional[PositiveInteger] = None
        self.key_slot_only: Optional[Boolean] = None
        self.key_slot_used_for: Optional[Boolean] = None
        self.latest_tx: Optional[Integer] = None
        self.listen_timeout: Optional[Integer] = None
        self.macro_initial: Optional[Integer] = None
        self.maximum: Optional[Integer] = None
        self.micro_initial: Optional[Integer] = None
        self.micro_per_cycle: Optional[Integer] = None
        self.microtick: Optional[TimeValue] = None
        self.nm_vector_early: Optional[Boolean] = None
        self.offset_correction: Optional[Integer] = None
        self.rate_correction: Optional[Integer] = None
        self.samples_per_microtick: Optional[Integer] = None
        self.second_key_slot: Optional[PositiveInteger] = None
        self.two_key_slot: Optional[Boolean] = None
        self.wake_up_pattern: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayCommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationController":
        """Create FlexrayCommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayCommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayCommunicationController since parent returns ARObject
        return cast("FlexrayCommunicationController", obj)


class FlexrayCommunicationControllerBuilder:
    """Builder for FlexrayCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationController = FlexrayCommunicationController()

    def build(self) -> FlexrayCommunicationController:
        """Build and return FlexrayCommunicationController object.

        Returns:
            FlexrayCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
