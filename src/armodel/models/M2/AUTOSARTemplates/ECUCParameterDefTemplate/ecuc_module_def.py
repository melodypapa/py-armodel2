"""EcucModuleDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 32)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import EcucDefinitionElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucModuleDef(EcucDefinitionElement):
    """AUTOSAR EcucModuleDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    api_service_prefix: Optional[CIdentifier]
    containers: list[EcucContainerDef]
    post_build_variant: Optional[Boolean]
    refined_module_ref: Optional[ARRef]
    supporteds: list[Any]
    def __init__(self) -> None:
        """Initialize EcucModuleDef."""
        super().__init__()
        self.api_service_prefix: Optional[CIdentifier] = None
        self.containers: list[EcucContainerDef] = []
        self.post_build_variant: Optional[Boolean] = None
        self.refined_module_ref: Optional[ARRef] = None
        self.supporteds: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucModuleDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucModuleDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize api_service_prefix
        if self.api_service_prefix is not None:
            serialized = SerializationHelper.serialize_item(self.api_service_prefix, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("API-SERVICE-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize post_build_variant
        if self.post_build_variant is not None:
            serialized = SerializationHelper.serialize_item(self.post_build_variant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize refined_module_ref
        if self.refined_module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.refined_module_ref, "EcucModuleDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFINED-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supporteds (list to container "SUPPORTEDS")
        if self.supporteds:
            wrapper = ET.Element("SUPPORTEDS")
            for item in self.supporteds:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleDef":
        """Deserialize XML element to EcucModuleDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucModuleDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucModuleDef, cls).deserialize(element)

        # Parse api_service_prefix
        child = SerializationHelper.find_child_element(element, "API-SERVICE-PREFIX")
        if child is not None:
            api_service_prefix_value = SerializationHelper.deserialize_by_tag(child, "CIdentifier")
            obj.api_service_prefix = api_service_prefix_value

        # Parse containers (list from container "CONTAINERS")
        obj.containers = []
        container = SerializationHelper.find_child_element(element, "CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.containers.append(child_value)

        # Parse post_build_variant
        child = SerializationHelper.find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        # Parse refined_module_ref
        child = SerializationHelper.find_child_element(element, "REFINED-MODULE-REF")
        if child is not None:
            refined_module_ref_value = ARRef.deserialize(child)
            obj.refined_module_ref = refined_module_ref_value

        # Parse supporteds (list from container "SUPPORTEDS")
        obj.supporteds = []
        container = SerializationHelper.find_child_element(element, "SUPPORTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.supporteds.append(child_value)

        return obj



class EcucModuleDefBuilder(EcucDefinitionElementBuilder):
    """Builder for EcucModuleDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucModuleDef = EcucModuleDef()


    def with_api_service_prefix(self, value: Optional[CIdentifier]) -> "EcucModuleDefBuilder":
        """Set api_service_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.api_service_prefix = value
        return self

    def with_containers(self, items: list[EcucContainerDef]) -> "EcucModuleDefBuilder":
        """Set containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.containers = list(items) if items else []
        return self

    def with_post_build_variant(self, value: Optional[Boolean]) -> "EcucModuleDefBuilder":
        """Set post_build_variant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.post_build_variant = value
        return self

    def with_refined_module(self, value: Optional[EcucModuleDef]) -> "EcucModuleDefBuilder":
        """Set refined_module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.refined_module = value
        return self

    def with_supporteds(self, items: list[any (EcucConfiguration)]) -> "EcucModuleDefBuilder":
        """Set supporteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.supporteds = list(items) if items else []
        return self


    def add_container(self, item: EcucContainerDef) -> "EcucModuleDefBuilder":
        """Add a single item to containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.containers.append(item)
        return self

    def clear_containers(self) -> "EcucModuleDefBuilder":
        """Clear all items from containers list.

        Returns:
            self for method chaining
        """
        self._obj.containers = []
        return self

    def add_supported(self, item: any (EcucConfiguration)) -> "EcucModuleDefBuilder":
        """Add a single item to supporteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.supporteds.append(item)
        return self

    def clear_supporteds(self) -> "EcucModuleDefBuilder":
        """Clear all items from supporteds list.

        Returns:
            self for method chaining
        """
        self._obj.supporteds = []
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


    def build(self) -> EcucModuleDef:
        """Build and return the EcucModuleDef instance with validation."""
        self._validate_instance()
        pass
        return self._obj