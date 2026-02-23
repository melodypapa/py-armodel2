"""CouplingPortRatePolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class CouplingPortRatePolicy(ARObject):
    """AUTOSAR CouplingPortRatePolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    policy_action: Optional[CouplingPortRatePolicy]
    priority: Optional[PositiveInteger]
    time_interval: Optional[TimeValue]
    v_lan_refs: list[Any]
    def __init__(self) -> None:
        """Initialize CouplingPortRatePolicy."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.policy_action: Optional[CouplingPortRatePolicy] = None
        self.priority: Optional[PositiveInteger] = None
        self.time_interval: Optional[TimeValue] = None
        self.v_lan_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortRatePolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortRatePolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize policy_action
        if self.policy_action is not None:
            serialized = SerializationHelper.serialize_item(self.policy_action, "CouplingPortRatePolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POLICY-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_interval
        if self.time_interval is not None:
            serialized = SerializationHelper.serialize_item(self.time_interval, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize v_lan_refs (list to container "V-LAN-REFS")
        if self.v_lan_refs:
            wrapper = ET.Element("V-LAN-REFS")
            for item in self.v_lan_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("V-LAN-REF")
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
    def deserialize(cls, element: ET.Element) -> "CouplingPortRatePolicy":
        """Deserialize XML element to CouplingPortRatePolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortRatePolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortRatePolicy, cls).deserialize(element)

        # Parse data_length
        child = SerializationHelper.find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse policy_action
        child = SerializationHelper.find_child_element(element, "POLICY-ACTION")
        if child is not None:
            policy_action_value = SerializationHelper.deserialize_by_tag(child, "CouplingPortRatePolicy")
            obj.policy_action = policy_action_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse time_interval
        child = SerializationHelper.find_child_element(element, "TIME-INTERVAL")
        if child is not None:
            time_interval_value = child.text
            obj.time_interval = time_interval_value

        # Parse v_lan_refs (list from container "V-LAN-REFS")
        obj.v_lan_refs = []
        container = SerializationHelper.find_child_element(element, "V-LAN-REFS")
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
                    obj.v_lan_refs.append(child_value)

        return obj



class CouplingPortRatePolicyBuilder(BuilderBase):
    """Builder for CouplingPortRatePolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortRatePolicy = CouplingPortRatePolicy()


    def with_data_length(self, value: Optional[PositiveInteger]) -> "CouplingPortRatePolicyBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_policy_action(self, value: Optional[CouplingPortRatePolicy]) -> "CouplingPortRatePolicyBuilder":
        """Set policy_action attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.policy_action = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "CouplingPortRatePolicyBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_time_interval(self, value: Optional[TimeValue]) -> "CouplingPortRatePolicyBuilder":
        """Set time_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_interval = value
        return self

    def with_v_lans(self, items: list[any (EthernetPhysical)]) -> "CouplingPortRatePolicyBuilder":
        """Set v_lans list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.v_lans = list(items) if items else []
        return self


    def add_v_lan(self, item: any (EthernetPhysical)) -> "CouplingPortRatePolicyBuilder":
        """Add a single item to v_lans list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.v_lans.append(item)
        return self

    def clear_v_lans(self) -> "CouplingPortRatePolicyBuilder":
        """Clear all items from v_lans list.

        Returns:
            self for method chaining
        """
        self._obj.v_lans = []
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


    def build(self) -> CouplingPortRatePolicy:
        """Build and return the CouplingPortRatePolicy instance with validation."""
        self._validate_instance()
        pass
        return self._obj