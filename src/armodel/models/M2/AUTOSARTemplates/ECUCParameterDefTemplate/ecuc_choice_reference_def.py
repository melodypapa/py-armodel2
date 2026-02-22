"""EcucChoiceReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 74)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucChoiceReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EcucChoiceReferenceDef."""
        super().__init__()
        self.destination_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucChoiceReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucChoiceReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_refs (list to container "DESTINATION-REFS")
        if self.destination_refs:
            wrapper = ET.Element("DESTINATION-REFS")
            for item in self.destination_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    child_elem = ET.Element("DESTINATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "EcucChoiceReferenceDef":
        """Deserialize XML element to EcucChoiceReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucChoiceReferenceDef, cls).deserialize(element)

        # Parse destination_refs (list from container "DESTINATION-REFS")
        obj.destination_refs = []
        container = SerializationHelper.find_child_element(element, "DESTINATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.destination_refs.append(child_value)

        return obj



class EcucChoiceReferenceDefBuilder:
    """Builder for EcucChoiceReferenceDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: EcucChoiceReferenceDef = EcucChoiceReferenceDef()


    def with_short_name(self, value: Identifier) -> "EcucChoiceReferenceDefBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "EcucChoiceReferenceDefBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "EcucChoiceReferenceDefBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_ecuc_cond(self, value: Optional[any (EcucCondition)]) -> "EcucChoiceReferenceDefBuilder":
        """Set ecuc_cond attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_cond = value
        return self

    def with_ecuc_validations(self, items: list[EcucValidationCondition]) -> "EcucChoiceReferenceDefBuilder":
        """Set ecuc_validations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = list(items) if items else []
        return self

    def with_lower_multiplicity(self, value: Optional[PositiveInteger]) -> "EcucChoiceReferenceDefBuilder":
        """Set lower_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lower_multiplicity = value
        return self

    def with_related_trace(self, value: Optional[Traceable]) -> "EcucChoiceReferenceDefBuilder":
        """Set related_trace attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.related_trace = value
        return self

    def with_scope(self, value: Optional[EcucScopeEnum]) -> "EcucChoiceReferenceDefBuilder":
        """Set scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scope = value
        return self

    def with_upper_multiplicity(self, value: Optional[Boolean]) -> "EcucChoiceReferenceDefBuilder":
        """Set upper_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_multiplicity = value
        return self

    def with_multiplicities(self, items: list[EcucMultiplicityConfigurationClass]) -> "EcucChoiceReferenceDefBuilder":
        """Set multiplicities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.multiplicities = list(items) if items else []
        return self

    def with_origin(self, value: Optional[String]) -> "EcucChoiceReferenceDefBuilder":
        """Set origin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.origin = value
        return self

    def with_post_build_variant(self, value: Optional[Boolean]) -> "EcucChoiceReferenceDefBuilder":
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

    def with_requires_index(self, value: Optional[Boolean]) -> "EcucChoiceReferenceDefBuilder":
        """Set requires_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requires_index = value
        return self

    def with_value_configs(self, items: list[EcucValueConfigurationClass]) -> "EcucChoiceReferenceDefBuilder":
        """Set value_configs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.value_configs = list(items) if items else []
        return self

    def with_with_auto(self, value: Optional[Boolean]) -> "EcucChoiceReferenceDefBuilder":
        """Set with_auto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.with_auto = value
        return self

    def with_requires(self, value: Optional[Boolean]) -> "EcucChoiceReferenceDefBuilder":
        """Set requires attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requires = value
        return self

    def with_destinations(self, items: list[EcucContainerDef]) -> "EcucChoiceReferenceDefBuilder":
        """Set destinations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.destinations = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_ecuc_validation(self, item: EcucValidationCondition) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to ecuc_validations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations.append(item)
        return self

    def clear_ecuc_validations(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from ecuc_validations list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = []
        return self

    def add_multiplicitie(self, item: EcucMultiplicityConfigurationClass) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to multiplicities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.multiplicities.append(item)
        return self

    def clear_multiplicities(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from multiplicities list.

        Returns:
            self for method chaining
        """
        self._obj.multiplicities = []
        return self

    def add_value_config(self, item: EcucValueConfigurationClass) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to value_configs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.value_configs.append(item)
        return self

    def clear_value_configs(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from value_configs list.

        Returns:
            self for method chaining
        """
        self._obj.value_configs = []
        return self

    def add_destination(self, item: EcucContainerDef) -> "EcucChoiceReferenceDefBuilder":
        """Add a single item to destinations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.destinations.append(item)
        return self

    def clear_destinations(self) -> "EcucChoiceReferenceDefBuilder":
        """Clear all items from destinations list.

        Returns:
            self for method chaining
        """
        self._obj.destinations = []
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


    def build(self) -> EcucChoiceReferenceDef:
        """Build and return the EcucChoiceReferenceDef instance with validation."""
        self._validate_instance()
        pass
        return self._obj