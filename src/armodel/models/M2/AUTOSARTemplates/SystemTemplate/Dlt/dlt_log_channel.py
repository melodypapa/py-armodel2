"""DltLogChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import (
    DltDefaultTraceStateEnum,
    LogTraceDefaultLogLevelEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DltLogChannel(Identifiable):
    """AUTOSAR DltLogChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[DltContext]
    default_trace: Optional[DltDefaultTraceStateEnum]
    dlt_messages: list[DltMessage]
    log_channel_id: Optional[String]
    log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum]
    non_verbose: Optional[Boolean]
    rx_pdu_triggering_channel_ref: Optional[ARRef]
    segmentation: Optional[Boolean]
    tx_pdu_triggering_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DltLogChannel."""
        super().__init__()
        self.applications: list[DltContext] = []
        self.default_trace: Optional[DltDefaultTraceStateEnum] = None
        self.dlt_messages: list[DltMessage] = []
        self.log_channel_id: Optional[String] = None
        self.log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum] = None
        self.non_verbose: Optional[Boolean] = None
        self.rx_pdu_triggering_channel_ref: Optional[ARRef] = None
        self.segmentation: Optional[Boolean] = None
        self.tx_pdu_triggering_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize DltLogChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltLogChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = ARObject._serialize_item(item, "DltContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize default_trace
        if self.default_trace is not None:
            serialized = ARObject._serialize_item(self.default_trace, "DltDefaultTraceStateEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-TRACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_messages (list to container "DLT-MESSAGES")
        if self.dlt_messages:
            wrapper = ET.Element("DLT-MESSAGES")
            for item in self.dlt_messages:
                serialized = ARObject._serialize_item(item, "DltMessage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize log_channel_id
        if self.log_channel_id is not None:
            serialized = ARObject._serialize_item(self.log_channel_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOG-CHANNEL-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize log_trace_default_log
        if self.log_trace_default_log is not None:
            serialized = ARObject._serialize_item(self.log_trace_default_log, "LogTraceDefaultLogLevelEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOG-TRACE-DEFAULT-LOG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize non_verbose
        if self.non_verbose is not None:
            serialized = ARObject._serialize_item(self.non_verbose, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NON-VERBOSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_pdu_triggering_channel_ref
        if self.rx_pdu_triggering_channel_ref is not None:
            serialized = ARObject._serialize_item(self.rx_pdu_triggering_channel_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-PDU-TRIGGERING-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segmentation
        if self.segmentation is not None:
            serialized = ARObject._serialize_item(self.segmentation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEGMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_pdu_triggering_ref
        if self.tx_pdu_triggering_ref is not None:
            serialized = ARObject._serialize_item(self.tx_pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-PDU-TRIGGERING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltLogChannel":
        """Deserialize XML element to DltLogChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltLogChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltLogChannel, cls).deserialize(element)

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = ARObject._find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse default_trace
        child = ARObject._find_child_element(element, "DEFAULT-TRACE")
        if child is not None:
            default_trace_value = DltDefaultTraceStateEnum.deserialize(child)
            obj.default_trace = default_trace_value

        # Parse dlt_messages (list from container "DLT-MESSAGES")
        obj.dlt_messages = []
        container = ARObject._find_child_element(element, "DLT-MESSAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_messages.append(child_value)

        # Parse log_channel_id
        child = ARObject._find_child_element(element, "LOG-CHANNEL-ID")
        if child is not None:
            log_channel_id_value = child.text
            obj.log_channel_id = log_channel_id_value

        # Parse log_trace_default_log
        child = ARObject._find_child_element(element, "LOG-TRACE-DEFAULT-LOG")
        if child is not None:
            log_trace_default_log_value = LogTraceDefaultLogLevelEnum.deserialize(child)
            obj.log_trace_default_log = log_trace_default_log_value

        # Parse non_verbose
        child = ARObject._find_child_element(element, "NON-VERBOSE")
        if child is not None:
            non_verbose_value = child.text
            obj.non_verbose = non_verbose_value

        # Parse rx_pdu_triggering_channel_ref
        child = ARObject._find_child_element(element, "RX-PDU-TRIGGERING-CHANNEL")
        if child is not None:
            rx_pdu_triggering_channel_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.rx_pdu_triggering_channel_ref = rx_pdu_triggering_channel_ref_value

        # Parse segmentation
        child = ARObject._find_child_element(element, "SEGMENTATION")
        if child is not None:
            segmentation_value = child.text
            obj.segmentation = segmentation_value

        # Parse tx_pdu_triggering_ref
        child = ARObject._find_child_element(element, "TX-PDU-TRIGGERING")
        if child is not None:
            tx_pdu_triggering_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.tx_pdu_triggering_ref = tx_pdu_triggering_ref_value

        return obj



class DltLogChannelBuilder:
    """Builder for DltLogChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltLogChannel = DltLogChannel()

    def build(self) -> DltLogChannel:
        """Build and return DltLogChannel object.

        Returns:
            DltLogChannel instance
        """
        # TODO: Add validation
        return self._obj
