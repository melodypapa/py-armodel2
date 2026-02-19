"""SwitchStreamFilterEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)


class SwitchStreamFilterEntry(Identifiable):
    """AUTOSAR SwitchStreamFilterEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous: Optional[CouplingPort]
    filter_priority: Optional[PositiveInteger]
    flow_metering: Optional[SwitchFlowMeteringEntry]
    max_sdu_size: Optional[PositiveInteger]
    stream_gate: Optional[SwitchStreamGateEntry]
    stream: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SwitchStreamFilterEntry."""
        super().__init__()
        self.asynchronous: Optional[CouplingPort] = None
        self.filter_priority: Optional[PositiveInteger] = None
        self.flow_metering: Optional[SwitchFlowMeteringEntry] = None
        self.max_sdu_size: Optional[PositiveInteger] = None
        self.stream_gate: Optional[SwitchStreamGateEntry] = None
        self.stream: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamFilterEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamFilterEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize asynchronous
        if self.asynchronous is not None:
            serialized = ARObject._serialize_item(self.asynchronous, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASYNCHRONOUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_priority
        if self.filter_priority is not None:
            serialized = ARObject._serialize_item(self.filter_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_metering
        if self.flow_metering is not None:
            serialized = ARObject._serialize_item(self.flow_metering, "SwitchFlowMeteringEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-METERING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sdu_size
        if self.max_sdu_size is not None:
            serialized = ARObject._serialize_item(self.max_sdu_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SDU-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stream_gate
        if self.stream_gate is not None:
            serialized = ARObject._serialize_item(self.stream_gate, "SwitchStreamGateEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-GATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stream
        if self.stream is not None:
            serialized = ARObject._serialize_item(self.stream, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterEntry":
        """Deserialize XML element to SwitchStreamFilterEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamFilterEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamFilterEntry, cls).deserialize(element)

        # Parse asynchronous
        child = ARObject._find_child_element(element, "ASYNCHRONOUS")
        if child is not None:
            asynchronous_value = ARObject._deserialize_by_tag(child, "CouplingPort")
            obj.asynchronous = asynchronous_value

        # Parse filter_priority
        child = ARObject._find_child_element(element, "FILTER-PRIORITY")
        if child is not None:
            filter_priority_value = child.text
            obj.filter_priority = filter_priority_value

        # Parse flow_metering
        child = ARObject._find_child_element(element, "FLOW-METERING")
        if child is not None:
            flow_metering_value = ARObject._deserialize_by_tag(child, "SwitchFlowMeteringEntry")
            obj.flow_metering = flow_metering_value

        # Parse max_sdu_size
        child = ARObject._find_child_element(element, "MAX-SDU-SIZE")
        if child is not None:
            max_sdu_size_value = child.text
            obj.max_sdu_size = max_sdu_size_value

        # Parse stream_gate
        child = ARObject._find_child_element(element, "STREAM-GATE")
        if child is not None:
            stream_gate_value = ARObject._deserialize_by_tag(child, "SwitchStreamGateEntry")
            obj.stream_gate = stream_gate_value

        # Parse stream
        child = ARObject._find_child_element(element, "STREAM")
        if child is not None:
            stream_value = child.text
            obj.stream = stream_value

        return obj



class SwitchStreamFilterEntryBuilder:
    """Builder for SwitchStreamFilterEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterEntry = SwitchStreamFilterEntry()

    def build(self) -> SwitchStreamFilterEntry:
        """Build and return SwitchStreamFilterEntry object.

        Returns:
            SwitchStreamFilterEntry instance
        """
        # TODO: Add validation
        return self._obj
