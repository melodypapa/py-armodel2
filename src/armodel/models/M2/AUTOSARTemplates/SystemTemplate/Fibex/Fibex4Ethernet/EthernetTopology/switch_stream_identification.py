"""SwitchStreamIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 135)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_rule import (
    SwitchStreamFilterRule,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwitchStreamIdentification(Identifiable):
    """AUTOSAR SwitchStreamIdentification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    egress_port_refs: list[ARRef]
    filter_action_block: Optional[Boolean]
    filter_action_dest: Optional[Any]
    filter_action_drop: Optional[Boolean]
    filter_action_vlan: Optional[PositiveInteger]
    ingress_port_refs: list[ARRef]
    stream_filter: Optional[SwitchStreamFilterRule]
    def __init__(self) -> None:
        """Initialize SwitchStreamIdentification."""
        super().__init__()
        self.egress_port_refs: list[ARRef] = []
        self.filter_action_block: Optional[Boolean] = None
        self.filter_action_dest: Optional[Any] = None
        self.filter_action_drop: Optional[Boolean] = None
        self.filter_action_vlan: Optional[PositiveInteger] = None
        self.ingress_port_refs: list[ARRef] = []
        self.stream_filter: Optional[SwitchStreamFilterRule] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamIdentification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamIdentification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize egress_port_refs (list to container "EGRESS-PORT-REFS")
        if self.egress_port_refs:
            wrapper = ET.Element("EGRESS-PORT-REFS")
            for item in self.egress_port_refs:
                serialized = SerializationHelper.serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("EGRESS-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize filter_action_block
        if self.filter_action_block is not None:
            serialized = SerializationHelper.serialize_item(self.filter_action_block, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_dest
        if self.filter_action_dest is not None:
            serialized = SerializationHelper.serialize_item(self.filter_action_dest, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-DEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_drop
        if self.filter_action_drop is not None:
            serialized = SerializationHelper.serialize_item(self.filter_action_drop, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-DROP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_vlan
        if self.filter_action_vlan is not None:
            serialized = SerializationHelper.serialize_item(self.filter_action_vlan, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ingress_port_refs (list to container "INGRESS-PORT-REFS")
        if self.ingress_port_refs:
            wrapper = ET.Element("INGRESS-PORT-REFS")
            for item in self.ingress_port_refs:
                serialized = SerializationHelper.serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("INGRESS-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stream_filter
        if self.stream_filter is not None:
            serialized = SerializationHelper.serialize_item(self.stream_filter, "SwitchStreamFilterRule")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamIdentification":
        """Deserialize XML element to SwitchStreamIdentification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamIdentification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamIdentification, cls).deserialize(element)

        # Parse egress_port_refs (list from container "EGRESS-PORT-REFS")
        obj.egress_port_refs = []
        container = SerializationHelper.find_child_element(element, "EGRESS-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.egress_port_refs.append(child_value)

        # Parse filter_action_block
        child = SerializationHelper.find_child_element(element, "FILTER-ACTION-BLOCK")
        if child is not None:
            filter_action_block_value = child.text
            obj.filter_action_block = filter_action_block_value

        # Parse filter_action_dest
        child = SerializationHelper.find_child_element(element, "FILTER-ACTION-DEST")
        if child is not None:
            filter_action_dest_value = child.text
            obj.filter_action_dest = filter_action_dest_value

        # Parse filter_action_drop
        child = SerializationHelper.find_child_element(element, "FILTER-ACTION-DROP")
        if child is not None:
            filter_action_drop_value = child.text
            obj.filter_action_drop = filter_action_drop_value

        # Parse filter_action_vlan
        child = SerializationHelper.find_child_element(element, "FILTER-ACTION-VLAN")
        if child is not None:
            filter_action_vlan_value = child.text
            obj.filter_action_vlan = filter_action_vlan_value

        # Parse ingress_port_refs (list from container "INGRESS-PORT-REFS")
        obj.ingress_port_refs = []
        container = SerializationHelper.find_child_element(element, "INGRESS-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ingress_port_refs.append(child_value)

        # Parse stream_filter
        child = SerializationHelper.find_child_element(element, "STREAM-FILTER")
        if child is not None:
            stream_filter_value = SerializationHelper.deserialize_by_tag(child, "SwitchStreamFilterRule")
            obj.stream_filter = stream_filter_value

        return obj



class SwitchStreamIdentificationBuilder(IdentifiableBuilder):
    """Builder for SwitchStreamIdentification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchStreamIdentification = SwitchStreamIdentification()


    def with_egress_ports(self, items: list[CouplingPort]) -> "SwitchStreamIdentificationBuilder":
        """Set egress_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.egress_ports = list(items) if items else []
        return self

    def with_filter_action_block(self, value: Optional[Boolean]) -> "SwitchStreamIdentificationBuilder":
        """Set filter_action_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_action_block = value
        return self

    def with_filter_action_dest(self, value: Optional[any (SwitchStreamFilter)]) -> "SwitchStreamIdentificationBuilder":
        """Set filter_action_dest attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_action_dest = value
        return self

    def with_filter_action_drop(self, value: Optional[Boolean]) -> "SwitchStreamIdentificationBuilder":
        """Set filter_action_drop attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_action_drop = value
        return self

    def with_filter_action_vlan(self, value: Optional[PositiveInteger]) -> "SwitchStreamIdentificationBuilder":
        """Set filter_action_vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_action_vlan = value
        return self

    def with_ingress_ports(self, items: list[CouplingPort]) -> "SwitchStreamIdentificationBuilder":
        """Set ingress_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ingress_ports = list(items) if items else []
        return self

    def with_stream_filter(self, value: Optional[SwitchStreamFilterRule]) -> "SwitchStreamIdentificationBuilder":
        """Set stream_filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stream_filter = value
        return self


    def add_egress_port(self, item: CouplingPort) -> "SwitchStreamIdentificationBuilder":
        """Add a single item to egress_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.egress_ports.append(item)
        return self

    def clear_egress_ports(self) -> "SwitchStreamIdentificationBuilder":
        """Clear all items from egress_ports list.

        Returns:
            self for method chaining
        """
        self._obj.egress_ports = []
        return self

    def add_ingress_port(self, item: CouplingPort) -> "SwitchStreamIdentificationBuilder":
        """Add a single item to ingress_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ingress_ports.append(item)
        return self

    def clear_ingress_ports(self) -> "SwitchStreamIdentificationBuilder":
        """Clear all items from ingress_ports list.

        Returns:
            self for method chaining
        """
        self._obj.ingress_ports = []
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


    def build(self) -> SwitchStreamIdentification:
        """Build and return the SwitchStreamIdentification instance with validation."""
        self._validate_instance()
        pass
        return self._obj