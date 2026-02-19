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
    def serialize(self) -> ET.Element:
        """Serialize PhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_connectors (list to container "COMM-CONNECTORS")
        if self.comm_connectors:
            wrapper = ET.Element("COMM-CONNECTORS")
            for item in self.comm_connectors:
                serialized = ARObject._serialize_item(item, "CommunicationConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize frame_triggering_refs (list to container "FRAME-TRIGGERINGS")
        if self.frame_triggering_refs:
            wrapper = ET.Element("FRAME-TRIGGERINGS")
            for item in self.frame_triggering_refs:
                serialized = ARObject._serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_refs (list to container "I-SIGNALS")
        if self.i_signal_refs:
            wrapper = ET.Element("I-SIGNALS")
            for item in self.i_signal_refs:
                serialized = ARObject._serialize_item(item, "ISignalTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize manageds (list to container "MANAGEDS")
        if self.manageds:
            wrapper = ET.Element("MANAGEDS")
            for item in self.manageds:
                serialized = ARObject._serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_triggering_refs (list to container "PDU-TRIGGERINGS")
        if self.pdu_triggering_refs:
            wrapper = ET.Element("PDU-TRIGGERINGS")
            for item in self.pdu_triggering_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalChannel":
        """Deserialize XML element to PhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalChannel, cls).deserialize(element)

        # Parse comm_connectors (list from container "COMM-CONNECTORS")
        obj.comm_connectors = []
        container = ARObject._find_child_element(element, "COMM-CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_connectors.append(child_value)

        # Parse frame_triggering_refs (list from container "FRAME-TRIGGERINGS")
        obj.frame_triggering_refs = []
        container = ARObject._find_child_element(element, "FRAME-TRIGGERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.frame_triggering_refs.append(child_value)

        # Parse i_signal_refs (list from container "I-SIGNALS")
        obj.i_signal_refs = []
        container = ARObject._find_child_element(element, "I-SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_refs.append(child_value)

        # Parse manageds (list from container "MANAGEDS")
        obj.manageds = []
        container = ARObject._find_child_element(element, "MANAGEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.manageds.append(child_value)

        # Parse pdu_triggering_refs (list from container "PDU-TRIGGERINGS")
        obj.pdu_triggering_refs = []
        container = ARObject._find_child_element(element, "PDU-TRIGGERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_triggering_refs.append(child_value)

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
