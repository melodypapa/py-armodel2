"""FrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 295)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 418)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 224)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_port import (
    FramePort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class FrameTriggering(Identifiable, ABC):
    """AUTOSAR FrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    frame: Optional[Frame]
    frame_ports: list[FramePort]
    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FrameTriggering."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.frame_ports: list[FramePort] = []
        self.pdu_triggering_refs: list[ARRef] = []


class FrameTriggeringBuilder:
    """Builder for FrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameTriggering = FrameTriggering()

    def build(self) -> FrameTriggering:
        """Build and return FrameTriggering object.

        Returns:
            FrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
