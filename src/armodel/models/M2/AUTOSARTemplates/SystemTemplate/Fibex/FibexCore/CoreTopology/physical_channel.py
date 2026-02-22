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
from armodel.serialization import SerializationHelper
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

    comm_connector_refs: list[ARRef]
    frame_triggering_refs: list[ARRef]
    i_signal_refs: list[ARRef]
    managed_refs: list[ARRef]
    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PhysicalChannel."""
        super().__init__()
        self.comm_connector_refs: list[ARRef] = []
        self.frame_triggering_refs: list[ARRef] = []
        self.i_signal_refs: list[ARRef] = []
        self.managed_refs: list[ARRef] = []
        self.pdu_triggering_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_connector_refs (list to container "COMM-CONNECTOR-REFS")
        if self.comm_connector_refs:
            wrapper = ET.Element("COMM-CONNECTOR-REFS")
            for item in self.comm_connector_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationConnector")
                if serialized is not None:
                    child_elem = ET.Element("COMM-CONNECTOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize frame_triggering_refs (list to container "FRAME-TRIGGERING-REFS")
        if self.frame_triggering_refs:
            wrapper = ET.Element("FRAME-TRIGGERING-REFS")
            for item in self.frame_triggering_refs:
                serialized = SerializationHelper.serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    child_elem = ET.Element("FRAME-TRIGGERING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_refs (list to container "I-SIGNAL-REFS")
        if self.i_signal_refs:
            wrapper = ET.Element("I-SIGNAL-REFS")
            for item in self.i_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalTriggering")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize managed_refs (list to container "MANAGED-REFS")
        if self.managed_refs:
            wrapper = ET.Element("MANAGED-REFS")
            for item in self.managed_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("MANAGED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_triggering_refs (list to container "PDU-TRIGGERING-REFS")
        if self.pdu_triggering_refs:
            wrapper = ET.Element("PDU-TRIGGERING-REFS")
            for item in self.pdu_triggering_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PDU-TRIGGERING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse comm_connector_refs (list from container "COMM-CONNECTOR-REFS")
        obj.comm_connector_refs = []
        container = SerializationHelper.find_child_element(element, "COMM-CONNECTOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_connector_refs.append(child_value)

        # Parse frame_triggering_refs (list from container "FRAME-TRIGGERING-REFS")
        obj.frame_triggering_refs = []
        container = SerializationHelper.find_child_element(element, "FRAME-TRIGGERING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.frame_triggering_refs.append(child_value)

        # Parse i_signal_refs (list from container "I-SIGNAL-REFS")
        obj.i_signal_refs = []
        container = SerializationHelper.find_child_element(element, "I-SIGNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_refs.append(child_value)

        # Parse managed_refs (list from container "MANAGED-REFS")
        obj.managed_refs = []
        container = SerializationHelper.find_child_element(element, "MANAGED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.managed_refs.append(child_value)

        # Parse pdu_triggering_refs (list from container "PDU-TRIGGERING-REFS")
        obj.pdu_triggering_refs = []
        container = SerializationHelper.find_child_element(element, "PDU-TRIGGERING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_triggering_refs.append(child_value)

        return obj



