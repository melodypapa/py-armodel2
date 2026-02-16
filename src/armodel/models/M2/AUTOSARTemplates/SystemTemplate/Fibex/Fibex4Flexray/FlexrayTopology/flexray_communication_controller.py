"""FlexrayCommunicationController AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accepted": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # accepted
        "allow_halt_due_to": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allowHaltDueTo
        "allow_passive_to": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allowPassiveTo
        "cluster_drift": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # clusterDrift
        "decoding": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # decoding
        "delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # delay
        "external_sync": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # externalSync
        "extern_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # externOffset
        "extern_rate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # externRate
        "fall_back_internal": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # fallBackInternal
        "flexray_fifos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (FlexrayFifo),
        ),  # flexrayFifos
        "key_slot_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keySlotID
        "key_slot_only": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keySlotOnly
        "key_slot_used_for": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keySlotUsedFor
        "latest_tx": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # latestTX
        "listen_timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # listenTimeout
        "macro_initial": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macroInitial
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximum
        "micro_initial": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # microInitial
        "micro_per_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # microPerCycle
        "microtick": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # microtick
        "nm_vector_early": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmVectorEarly
        "offset_correction": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offsetCorrection
        "rate_correction": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rateCorrection
        "samples_per_microtick": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # samplesPerMicrotick
        "second_key_slot": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # secondKeySlot
        "two_key_slot": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # twoKeySlot
        "wake_up_pattern": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeUpPattern
    }

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
