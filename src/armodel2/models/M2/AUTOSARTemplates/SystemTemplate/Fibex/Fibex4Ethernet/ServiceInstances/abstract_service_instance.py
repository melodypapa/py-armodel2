"""AbstractServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

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
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue.tag_with_optional_value import (
    TagWithOptionalValue,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractServiceInstance(Identifiable, ABC):
    """AUTOSAR AbstractServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    capabilities: list[TagWithOptionalValue]
    major_version: Optional[PositiveInteger]
    method: Optional[PduActivationRoutingGroup]
    routing_group_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CAPABILITYS": lambda obj, elem: obj.capabilities.append(SerializationHelper.deserialize_by_tag(elem, "TagWithOptionalValue")),
        "MAJOR-VERSION": lambda obj, elem: setattr(obj, "major_version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "METHOD": lambda obj, elem: setattr(obj, "method", SerializationHelper.deserialize_by_tag(elem, "PduActivationRoutingGroup")),
        "ROUTING-GROUP-REFS": lambda obj, elem: [obj.routing_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize AbstractServiceInstance."""
        super().__init__()
        self.capabilities: list[TagWithOptionalValue] = []
        self.major_version: Optional[PositiveInteger] = None
        self.method: Optional[PduActivationRoutingGroup] = None
        self.routing_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize AbstractServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize capabilities (list to container "CAPABILITYS")
        if self.capabilities:
            wrapper = ET.Element("CAPABILITYS")
            for item in self.capabilities:
                serialized = SerializationHelper.serialize_item(item, "TagWithOptionalValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize major_version
        if self.major_version is not None:
            serialized = SerializationHelper.serialize_item(self.major_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAJOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize method
        if self.method is not None:
            serialized = SerializationHelper.serialize_item(self.method, "PduActivationRoutingGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("METHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routing_group_refs (list to container "ROUTING-GROUP-REFS")
        if self.routing_group_refs:
            wrapper = ET.Element("ROUTING-GROUP-REFS")
            for item in self.routing_group_refs:
                serialized = SerializationHelper.serialize_item(item, "SoAdRoutingGroup")
                if serialized is not None:
                    child_elem = ET.Element("ROUTING-GROUP-REF")
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
    def deserialize(cls, element: ET.Element) -> "AbstractServiceInstance":
        """Deserialize XML element to AbstractServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAPABILITYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.capabilities.append(SerializationHelper.deserialize_by_tag(item_elem, "TagWithOptionalValue"))
            elif tag == "MAJOR-VERSION":
                setattr(obj, "major_version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "METHOD":
                setattr(obj, "method", SerializationHelper.deserialize_by_tag(child, "PduActivationRoutingGroup"))
            elif tag == "ROUTING-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.routing_group_refs.append(ARRef.deserialize(item_elem))

        return obj



class AbstractServiceInstanceBuilder(IdentifiableBuilder):
    """Builder for AbstractServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractServiceInstance = AbstractServiceInstance()


    def with_capabilities(self, items: list[TagWithOptionalValue]) -> "AbstractServiceInstanceBuilder":
        """Set capabilities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.capabilities = list(items) if items else []
        return self

    def with_major_version(self, value: Optional[PositiveInteger]) -> "AbstractServiceInstanceBuilder":
        """Set major_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.major_version = value
        return self

    def with_method(self, value: Optional[PduActivationRoutingGroup]) -> "AbstractServiceInstanceBuilder":
        """Set method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.method = value
        return self

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "AbstractServiceInstanceBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self


    def add_capability(self, item: TagWithOptionalValue) -> "AbstractServiceInstanceBuilder":
        """Add a single item to capabilities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.capabilities.append(item)
        return self

    def clear_capabilities(self) -> "AbstractServiceInstanceBuilder":
        """Clear all items from capabilities list.

        Returns:
            self for method chaining
        """
        self._obj.capabilities = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "AbstractServiceInstanceBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "AbstractServiceInstanceBuilder":
        """Clear all items from routing_groups list.

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    @abstractmethod
    def build(self) -> AbstractServiceInstance:
        """Build and return the AbstractServiceInstance instance (abstract)."""
        raise NotImplementedError