"""EcucModuleConfigurationValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 441)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
        BswImplementation,
    )



class EcucModuleConfigurationValues(ARElement):
    """AUTOSAR EcucModuleConfigurationValues."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    containers: list[EcucContainerValue]
    definition_ref: Optional[ARRef]
    ecuc_def_edition: Optional[RevisionLabelString]
    implementation: Optional[Any]
    module_ref: Optional[ARRef]
    post_build_variant: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucModuleConfigurationValues."""
        super().__init__()
        self.containers: list[EcucContainerValue] = []
        self.definition_ref: Optional[ARRef] = None
        self.ecuc_def_edition: Optional[RevisionLabelString] = None
        self.implementation: Optional[Any] = None
        self.module_ref: Optional[ARRef] = None
        self.post_build_variant: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucModuleConfigurationValues to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucModuleConfigurationValues, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize definition_ref
        if self.definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.definition_ref, "EcucModuleDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_def_edition
        if self.ecuc_def_edition is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_def_edition, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-DEF-EDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation
        if self.implementation is not None:
            serialized = SerializationHelper.serialize_item(self.implementation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize module_ref
        if self.module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.module_ref, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleConfigurationValues":
        """Deserialize XML element to EcucModuleConfigurationValues object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucModuleConfigurationValues object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucModuleConfigurationValues, cls).deserialize(element)

        # Parse containers (list from container "CONTAINERS")
        obj.containers = []
        container = SerializationHelper.find_child_element(element, "CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.containers.append(child_value)

        # Parse definition_ref
        child = SerializationHelper.find_child_element(element, "DEFINITION-REF")
        if child is not None:
            definition_ref_value = ARRef.deserialize(child)
            obj.definition_ref = definition_ref_value

        # Parse ecuc_def_edition
        child = SerializationHelper.find_child_element(element, "ECUC-DEF-EDITION")
        if child is not None:
            ecuc_def_edition_value = child.text
            obj.ecuc_def_edition = ecuc_def_edition_value

        # Parse implementation
        child = SerializationHelper.find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = child.text
            obj.implementation = implementation_value

        # Parse module_ref
        child = SerializationHelper.find_child_element(element, "MODULE-REF")
        if child is not None:
            module_ref_value = ARRef.deserialize(child)
            obj.module_ref = module_ref_value

        # Parse post_build_variant
        child = SerializationHelper.find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        return obj



class EcucModuleConfigurationValuesBuilder:
    """Builder for EcucModuleConfigurationValues with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: EcucModuleConfigurationValues = EcucModuleConfigurationValues()


    def with_short_name(self, value: Identifier) -> "EcucModuleConfigurationValuesBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "EcucModuleConfigurationValuesBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "EcucModuleConfigurationValuesBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "EcucModuleConfigurationValuesBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "EcucModuleConfigurationValuesBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "EcucModuleConfigurationValuesBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "EcucModuleConfigurationValuesBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EcucModuleConfigurationValuesBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "EcucModuleConfigurationValuesBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_containers(self, items: list[EcucContainerValue]) -> "EcucModuleConfigurationValuesBuilder":
        """Set containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.containers = list(items) if items else []
        return self

    def with_definition(self, value: Optional[EcucModuleDef]) -> "EcucModuleConfigurationValuesBuilder":
        """Set definition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.definition = value
        return self

    def with_ecuc_def_edition(self, value: Optional[RevisionLabelString]) -> "EcucModuleConfigurationValuesBuilder":
        """Set ecuc_def_edition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_def_edition = value
        return self

    def with_implementation(self, value: Optional[any (EcucConfiguration)]) -> "EcucModuleConfigurationValuesBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_module(self, value: Optional[BswImplementation]) -> "EcucModuleConfigurationValuesBuilder":
        """Set module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.module = value
        return self

    def with_post_build_variant(self, value: Optional[Boolean]) -> "EcucModuleConfigurationValuesBuilder":
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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "EcucModuleConfigurationValuesBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "EcucModuleConfigurationValuesBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "EcucModuleConfigurationValuesBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EcucModuleConfigurationValuesBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_container(self, item: EcucContainerValue) -> "EcucModuleConfigurationValuesBuilder":
        """Add a single item to containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.containers.append(item)
        return self

    def clear_containers(self) -> "EcucModuleConfigurationValuesBuilder":
        """Clear all items from containers list.

        Returns:
            self for method chaining
        """
        self._obj.containers = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> EcucModuleConfigurationValues:
        """Build and return the EcucModuleConfigurationValues instance with validation."""
        self._validate_instance()
        pass
        return self._obj