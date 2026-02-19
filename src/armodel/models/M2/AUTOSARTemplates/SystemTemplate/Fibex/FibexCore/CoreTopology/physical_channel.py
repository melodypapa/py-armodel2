"""PhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 58)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod


class PhysicalChannel(Identifiable, ABC):
    """AUTOSAR PhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    comm_connectors: list[CommunicationConnector]
    frame_triggering_refs: list[ARRef]
    i_signal_refs: list[ARRef]
    manageds: list[PhysicalChannel]
    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PhysicalChannel."""
        super().__init__()
        self.comm_connectors: list[CommunicationConnector] = []
        self.frame_triggering_refs: list[ARRef] = []
        self.i_signal_refs: list[ARRef] = []
        self.manageds: list[PhysicalChannel] = []
        self.pdu_triggering_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalChannel":
        """Deserialize XML element to PhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse comm_connectors (list)
        obj.comm_connectors = []
        for child in ARObject._find_all_child_elements(element, "COMM-CONNECTORS"):
            comm_connectors_value = ARObject._deserialize_by_tag(child, "CommunicationConnector")
            obj.comm_connectors.append(comm_connectors_value)

        # Parse frame_triggering_refs (list)
        obj.frame_triggering_refs = []
        for child in ARObject._find_all_child_elements(element, "FRAME-TRIGGERINGS"):
            frame_triggering_refs_value = ARObject._deserialize_by_tag(child, "FrameTriggering")
            obj.frame_triggering_refs.append(frame_triggering_refs_value)

        # Parse i_signal_refs (list)
        obj.i_signal_refs = []
        for child in ARObject._find_all_child_elements(element, "I-SIGNALS"):
            i_signal_refs_value = ARObject._deserialize_by_tag(child, "ISignalTriggering")
            obj.i_signal_refs.append(i_signal_refs_value)

        # Parse manageds (list)
        obj.manageds = []
        for child in ARObject._find_all_child_elements(element, "MANAGEDS"):
            manageds_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.manageds.append(manageds_value)

        # Parse pdu_triggering_refs (list)
        obj.pdu_triggering_refs = []
        for child in ARObject._find_all_child_elements(element, "PDU-TRIGGERINGS"):
            pdu_triggering_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_triggering_refs.append(pdu_triggering_refs_value)

        return obj



class PhysicalChannelBuilder:
    """Builder for PhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalChannel = PhysicalChannel()

    def build(self) -> PhysicalChannel:
        """Build and return PhysicalChannel object.

        Returns:
            PhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
