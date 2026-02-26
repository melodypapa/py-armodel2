"""ServiceInstanceCollectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ServiceInstanceCollectionSet(FibexElement):
    """AUTOSAR ServiceInstanceCollectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_instances: list[AbstractServiceInstance]
    def __init__(self) -> None:
        """Initialize ServiceInstanceCollectionSet."""
        super().__init__()
        self.service_instances: list[AbstractServiceInstance] = []

    def serialize(self) -> ET.Element:
        """Serialize ServiceInstanceCollectionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServiceInstanceCollectionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize service_instances (list to container "SERVICE-INSTANCES")
        if self.service_instances:
            wrapper = ET.Element("SERVICE-INSTANCES")
            for item in self.service_instances:
                serialized = SerializationHelper.serialize_item(item, "AbstractServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceInstanceCollectionSet":
        """Deserialize XML element to ServiceInstanceCollectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceInstanceCollectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServiceInstanceCollectionSet, cls).deserialize(element)

        # Parse service_instances (list from container "SERVICE-INSTANCES")
        obj.service_instances = []
        container = SerializationHelper.find_child_element(element, "SERVICE-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_instances.append(child_value)

        return obj



class ServiceInstanceCollectionSetBuilder(FibexElementBuilder):
    """Builder for ServiceInstanceCollectionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ServiceInstanceCollectionSet = ServiceInstanceCollectionSet()


    def with_service_instances(self, items: list[AbstractServiceInstance]) -> "ServiceInstanceCollectionSetBuilder":
        """Set service_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_instances = list(items) if items else []
        return self


    def add_service_instance(self, item: AbstractServiceInstance) -> "ServiceInstanceCollectionSetBuilder":
        """Add a single item to service_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_instances.append(item)
        return self

    def clear_service_instances(self) -> "ServiceInstanceCollectionSetBuilder":
        """Clear all items from service_instances list.

        Returns:
            self for method chaining
        """
        self._obj.service_instances = []
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


    def build(self) -> ServiceInstanceCollectionSet:
        """Build and return the ServiceInstanceCollectionSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj