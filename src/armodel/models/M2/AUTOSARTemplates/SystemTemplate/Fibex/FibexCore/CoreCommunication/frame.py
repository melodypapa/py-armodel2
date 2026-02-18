"""Frame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 295)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 418)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 224)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
    PduToFrameMapping,
)
from abc import ABC, abstractmethod


class Frame(FibexElement, ABC):
    """AUTOSAR Frame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    frame_length: Optional[Integer]
    pdu_to_frames: list[PduToFrameMapping]
    def __init__(self) -> None:
        """Initialize Frame."""
        super().__init__()
        self.frame_length: Optional[Integer] = None
        self.pdu_to_frames: list[PduToFrameMapping] = []


class FrameBuilder:
    """Builder for Frame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Frame = Frame()

    def build(self) -> Frame:
        """Build and return Frame object.

        Returns:
            Frame instance
        """
        # TODO: Add validation
        return self._obj
