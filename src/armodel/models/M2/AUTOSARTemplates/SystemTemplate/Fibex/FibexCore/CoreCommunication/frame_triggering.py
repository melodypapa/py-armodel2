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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrameTriggering":
        """Deserialize XML element to FrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FrameTriggering object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = ARObject._deserialize_by_tag(child, "Frame")
            obj.frame = frame_value

        # Parse frame_ports (list)
        obj.frame_ports = []
        for child in ARObject._find_all_child_elements(element, "FRAME-PORTS"):
            frame_ports_value = ARObject._deserialize_by_tag(child, "FramePort")
            obj.frame_ports.append(frame_ports_value)

        # Parse pdu_triggering_refs (list)
        obj.pdu_triggering_refs = []
        for child in ARObject._find_all_child_elements(element, "PDU-TRIGGERINGS"):
            pdu_triggering_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_triggering_refs.append(pdu_triggering_refs_value)

        return obj



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
