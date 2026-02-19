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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMapping, cls).deserialize(element)

        # Parse mirroring
        child = ARObject._find_child_element(element, "MIRRORING")
        if child is not None:
            mirroring_value = MirroringProtocolEnum.deserialize(child)
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

        # Parse target_pdu_refs (list from container "TARGET-PDUS")
        obj.target_pdu_refs = []
        container = ARObject._find_child_element(element, "TARGET-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.target_pdu_refs.append(child_value)

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
