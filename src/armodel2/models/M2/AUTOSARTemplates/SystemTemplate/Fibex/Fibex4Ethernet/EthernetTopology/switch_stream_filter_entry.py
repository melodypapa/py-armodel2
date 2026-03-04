"""SwitchStreamFilterEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwitchStreamFilterEntry(Identifiable):
    """AUTOSAR SwitchStreamFilterEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWITCH-STREAM-FILTER-ENTRY"


    asynchronous_ref: Optional[ARRef]
    filter_priority: Optional[PositiveInteger]
    flow_metering_ref: Optional[ARRef]
    max_sdu_size: Optional[PositiveInteger]
    stream_gate_ref: Optional[ARRef]
    stream: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ASYNCHRONOUS-REF": lambda obj, elem: setattr(obj, "asynchronous_ref", ARRef.deserialize(elem)),
        "FILTER-PRIORITY": lambda obj, elem: setattr(obj, "filter_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "FLOW-METERING-REF": lambda obj, elem: setattr(obj, "flow_metering_ref", ARRef.deserialize(elem)),
        "MAX-SDU-SIZE": lambda obj, elem: setattr(obj, "max_sdu_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "STREAM-GATE-REF": lambda obj, elem: setattr(obj, "stream_gate_ref", ARRef.deserialize(elem)),
        "STREAM": lambda obj, elem: setattr(obj, "stream", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize SwitchStreamFilterEntry."""
        super().__init__()
        self.asynchronous_ref: Optional[ARRef] = None
        self.filter_priority: Optional[PositiveInteger] = None
        self.flow_metering_ref: Optional[ARRef] = None
        self.max_sdu_size: Optional[PositiveInteger] = None
        self.stream_gate_ref: Optional[ARRef] = None
        self.stream: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamFilterEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamFilterEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize asynchronous_ref
        if self.asynchronous_ref is not None:
            serialized = SerializationHelper.serialize_item(self.asynchronous_ref, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASYNCHRONOUS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_priority
        if self.filter_priority is not None:
            serialized = SerializationHelper.serialize_item(self.filter_priority, "PositiveInteger")
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

        # Serialize flow_metering_ref
        if self.flow_metering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flow_metering_ref, "SwitchFlowMeteringEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-METERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sdu_size
        if self.max_sdu_size is not None:
            serialized = SerializationHelper.serialize_item(self.max_sdu_size, "PositiveInteger")
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

        # Serialize stream_gate_ref
        if self.stream_gate_ref is not None:
            serialized = SerializationHelper.serialize_item(self.stream_gate_ref, "SwitchStreamGateEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-GATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stream
        if self.stream is not None:
            serialized = SerializationHelper.serialize_item(self.stream, "Boolean")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASYNCHRONOUS-REF":
                setattr(obj, "asynchronous_ref", ARRef.deserialize(child))
            elif tag == "FILTER-PRIORITY":
                setattr(obj, "filter_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "FLOW-METERING-REF":
                setattr(obj, "flow_metering_ref", ARRef.deserialize(child))
            elif tag == "MAX-SDU-SIZE":
                setattr(obj, "max_sdu_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "STREAM-GATE-REF":
                setattr(obj, "stream_gate_ref", ARRef.deserialize(child))
            elif tag == "STREAM":
                setattr(obj, "stream", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class SwitchStreamFilterEntryBuilder(IdentifiableBuilder):
    """Builder for SwitchStreamFilterEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchStreamFilterEntry = SwitchStreamFilterEntry()


    def with_asynchronous(self, value: Optional[CouplingPort]) -> "SwitchStreamFilterEntryBuilder":
        """Set asynchronous attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.asynchronous = value
        return self

    def with_filter_priority(self, value: Optional[PositiveInteger]) -> "SwitchStreamFilterEntryBuilder":
        """Set filter_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_priority = value
        return self

    def with_flow_metering(self, value: Optional[SwitchFlowMeteringEntry]) -> "SwitchStreamFilterEntryBuilder":
        """Set flow_metering attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flow_metering = value
        return self

    def with_max_sdu_size(self, value: Optional[PositiveInteger]) -> "SwitchStreamFilterEntryBuilder":
        """Set max_sdu_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_sdu_size = value
        return self

    def with_stream_gate(self, value: Optional[SwitchStreamGateEntry]) -> "SwitchStreamFilterEntryBuilder":
        """Set stream_gate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stream_gate = value
        return self

    def with_stream(self, value: Optional[Boolean]) -> "SwitchStreamFilterEntryBuilder":
        """Set stream attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stream = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "asynchronous",
        "filterPriority",
        "flowMetering",
        "maxSduSize",
        "stream",
        "streamGate",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwitchStreamFilterEntry:
        """Build and return the SwitchStreamFilterEntry instance with validation."""
        self._validate_instance()
        return self._obj