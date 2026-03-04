"""CouplingPortRatePolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortRatePolicy(ARObject):
    """AUTOSAR CouplingPortRatePolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-RATE-POLICY"


    data_length: Optional[PositiveInteger]
    policy_action: Optional[CouplingPortRatePolicy]
    priority: Optional[PositiveInteger]
    time_interval: Optional[TimeValue]
    v_lan_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "DATA-LENGTH": lambda obj, elem: setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "POLICY-ACTION": lambda obj, elem: setattr(obj, "policy_action", SerializationHelper.deserialize_by_tag(elem, "CouplingPortRatePolicy")),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-INTERVAL": lambda obj, elem: setattr(obj, "time_interval", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "V-LAN-REFS": lambda obj, elem: [obj.v_lan_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-LENGTH":
                setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "POLICY-ACTION":
                setattr(obj, "policy_action", SerializationHelper.deserialize_by_tag(child, "CouplingPortRatePolicy"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-INTERVAL":
                setattr(obj, "time_interval", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "V-LAN-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.v_lan_refs.append(ARRef.deserialize(item_elem))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataLength",
        "policyAction",
        "priority",
        "timeInterval",
        "vLan",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CouplingPortRatePolicy:
        """Build and return the CouplingPortRatePolicy instance with validation."""
        self._validate_instance()
        return self._obj