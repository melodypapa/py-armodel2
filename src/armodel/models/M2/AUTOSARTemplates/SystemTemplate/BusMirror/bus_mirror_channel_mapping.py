"""BusMirrorChannelMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 697)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    MirroringProtocolEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel import (
    BusMirrorChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class BusMirrorChannelMapping(FibexElement, ABC):
    """AUTOSAR BusMirrorChannelMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    mirroring: Optional[MirroringProtocolEnum]
    source_channel: Optional[BusMirrorChannel]
    target_channel: Optional[BusMirrorChannel]
    target_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMapping."""
        super().__init__()
        self.mirroring: Optional[MirroringProtocolEnum] = None
        self.source_channel: Optional[BusMirrorChannel] = None
        self.target_channel: Optional[BusMirrorChannel] = None
        self.target_pdu_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMapping":
        """Deserialize XML element to BusMirrorChannelMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mirroring
        child = ARObject._find_child_element(element, "MIRRORING")
        if child is not None:
            mirroring_value = child.text
            obj.mirroring = mirroring_value

        # Parse source_channel
        child = ARObject._find_child_element(element, "SOURCE-CHANNEL")
        if child is not None:
            source_channel_value = ARObject._deserialize_by_tag(child, "BusMirrorChannel")
            obj.source_channel = source_channel_value

        # Parse target_channel
        child = ARObject._find_child_element(element, "TARGET-CHANNEL")
        if child is not None:
            target_channel_value = ARObject._deserialize_by_tag(child, "BusMirrorChannel")
            obj.target_channel = target_channel_value

        # Parse target_pdu_refs (list)
        obj.target_pdu_refs = []
        for child in ARObject._find_all_child_elements(element, "TARGET-PDUS"):
            target_pdu_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.target_pdu_refs.append(target_pdu_refs_value)

        return obj



class BusMirrorChannelMappingBuilder:
    """Builder for BusMirrorChannelMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMapping = BusMirrorChannelMapping()

    def build(self) -> BusMirrorChannelMapping:
        """Build and return BusMirrorChannelMapping object.

        Returns:
            BusMirrorChannelMapping instance
        """
        # TODO: Add validation
        return self._obj
