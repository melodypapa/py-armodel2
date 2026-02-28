"""ConsumedProvidedServiceInstanceGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 523)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP"


    consumed_service_refs: list[Any]
    provided_service_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CONSUMED-SERVICES": lambda obj, elem: obj.consumed_service_refs.append(ARRef.deserialize(elem)),
        "PROVIDED-SERVICES": lambda obj, elem: obj.provided_service_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_service_refs: list[Any] = []
        self.provided_service_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsumedProvidedServiceInstanceGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedProvidedServiceInstanceGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consumed_service_refs (list to container "CONSUMED-SERVICE-REFS")
        if self.consumed_service_refs:
            wrapper = ET.Element("CONSUMED-SERVICE-REFS")
            for item in self.consumed_service_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONSUMED-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_service_refs (list to container "PROVIDED-SERVICE-REFS")
        if self.provided_service_refs:
            wrapper = ET.Element("PROVIDED-SERVICE-REFS")
            for item in self.provided_service_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-SERVICE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ConsumedProvidedServiceInstanceGroup":
        """Deserialize XML element to ConsumedProvidedServiceInstanceGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedProvidedServiceInstanceGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedProvidedServiceInstanceGroup, cls).deserialize(element)

        # Parse consumed_service_refs (list from container "CONSUMED-SERVICE-REFS")
        obj.consumed_service_refs = []
        container = SerializationHelper.find_child_element(element, "CONSUMED-SERVICE-REFS")
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
                    obj.consumed_service_refs.append(child_value)

        # Parse provided_service_refs (list from container "PROVIDED-SERVICE-REFS")
        obj.provided_service_refs = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-SERVICE-REFS")
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
                    obj.provided_service_refs.append(child_value)

        return obj



class ConsumedProvidedServiceInstanceGroupBuilder(FibexElementBuilder):
    """Builder for ConsumedProvidedServiceInstanceGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()


    def with_consumed_services(self, items: list[any (ConsumedService)]) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Set consumed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_services = list(items) if items else []
        return self

    def with_provided_services(self, items: list[any (ProvidedService)]) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Set provided_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_services = list(items) if items else []
        return self


    def add_consumed_service(self, item: any (ConsumedService)) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Add a single item to consumed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_services.append(item)
        return self

    def clear_consumed_services(self) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Clear all items from consumed_services list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_services = []
        return self

    def add_provided_service(self, item: any (ProvidedService)) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Add a single item to provided_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_services.append(item)
        return self

    def clear_provided_services(self) -> "ConsumedProvidedServiceInstanceGroupBuilder":
        """Clear all items from provided_services list.

        Returns:
            self for method chaining
        """
        self._obj.provided_services = []
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


    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return the ConsumedProvidedServiceInstanceGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj