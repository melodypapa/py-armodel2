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
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwitchStreamFilterEntry(Identifiable):
    """AUTOSAR SwitchStreamFilterEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous_ref: Optional[ARRef]
    filter_priority: Optional[PositiveInteger]
    flow_metering_ref: Optional[ARRef]
    max_sdu_size: Optional[PositiveInteger]
    stream_gate_ref: Optional[ARRef]
    stream: Optional[Boolean]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse asynchronous_ref
        child = SerializationHelper.find_child_element(element, "ASYNCHRONOUS-REF")
        if child is not None:
            asynchronous_ref_value = ARRef.deserialize(child)
            obj.asynchronous_ref = asynchronous_ref_value

        # Parse filter_priority
        child = SerializationHelper.find_child_element(element, "FILTER-PRIORITY")
        if child is not None:
            filter_priority_value = child.text
            obj.filter_priority = filter_priority_value

        # Parse flow_metering_ref
        child = SerializationHelper.find_child_element(element, "FLOW-METERING-REF")
        if child is not None:
            flow_metering_ref_value = ARRef.deserialize(child)
            obj.flow_metering_ref = flow_metering_ref_value

        # Parse max_sdu_size
        child = SerializationHelper.find_child_element(element, "MAX-SDU-SIZE")
        if child is not None:
            max_sdu_size_value = child.text
            obj.max_sdu_size = max_sdu_size_value

        # Parse stream_gate_ref
        child = SerializationHelper.find_child_element(element, "STREAM-GATE-REF")
        if child is not None:
            stream_gate_ref_value = ARRef.deserialize(child)
            obj.stream_gate_ref = stream_gate_ref_value

        # Parse stream
        child = SerializationHelper.find_child_element(element, "STREAM")
        if child is not None:
            stream_value = child.text
            obj.stream = stream_value

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




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SwitchStreamFilterEntry:
        """Build and return the SwitchStreamFilterEntry instance with validation."""
        self._validate_instance()
        pass
        return self._obj