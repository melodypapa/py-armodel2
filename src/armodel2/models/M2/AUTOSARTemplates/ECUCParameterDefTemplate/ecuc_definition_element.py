"""EcucDefinitionElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 45)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucScopeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
        EcucValidationCondition,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDefinitionElement(Identifiable, ABC):
    """AUTOSAR EcucDefinitionElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    ecuc_cond: Optional[Any]
    ecuc_validations: list[EcucValidationCondition]
    lower_multiplicity: Optional[PositiveInteger]
    related_trace_ref: Optional[ARRef]
    scope: Optional[EcucScopeEnum]
    upper_multiplicity: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ECUC-COND": lambda obj, elem: setattr(obj, "ecuc_cond", any (EcucCondition).deserialize(elem)),
        "ECUC-VALIDATIONS": lambda obj, elem: obj.ecuc_validations.append(EcucValidationCondition.deserialize(elem)),
        "LOWER-MULTIPLICITY": lambda obj, elem: setattr(obj, "lower_multiplicity", elem.text),
        "RELATED-TRACE-REF": lambda obj, elem: setattr(obj, "related_trace_ref", ARRef.deserialize(elem)),
        "SCOPE": lambda obj, elem: setattr(obj, "scope", EcucScopeEnum.deserialize(elem)),
        "UPPER-MULTIPLICITY": lambda obj, elem: setattr(obj, "upper_multiplicity", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EcucDefinitionElement."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.ecuc_validations: list[EcucValidationCondition] = []
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.related_trace_ref: Optional[ARRef] = None
        self.scope: Optional[EcucScopeEnum] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucDefinitionElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDefinitionElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_cond
        if self.ecuc_cond is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_cond, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-COND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_validations (list to container "ECUC-VALIDATIONS")
        if self.ecuc_validations:
            wrapper = ET.Element("ECUC-VALIDATIONS")
            for item in self.ecuc_validations:
                serialized = SerializationHelper.serialize_item(item, "EcucValidationCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lower_multiplicity
        if self.lower_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.lower_multiplicity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize related_trace_ref
        if self.related_trace_ref is not None:
            serialized = SerializationHelper.serialize_item(self.related_trace_ref, "Traceable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELATED-TRACE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope
        if self.scope is not None:
            serialized = SerializationHelper.serialize_item(self.scope, "EcucScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_multiplicity
        if self.upper_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.upper_multiplicity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionElement":
        """Deserialize XML element to EcucDefinitionElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDefinitionElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDefinitionElement, cls).deserialize(element)

        # Parse ecuc_cond
        child = SerializationHelper.find_child_element(element, "ECUC-COND")
        if child is not None:
            ecuc_cond_value = child.text
            obj.ecuc_cond = ecuc_cond_value

        # Parse ecuc_validations (list from container "ECUC-VALIDATIONS")
        obj.ecuc_validations = []
        container = SerializationHelper.find_child_element(element, "ECUC-VALIDATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecuc_validations.append(child_value)

        # Parse lower_multiplicity
        child = SerializationHelper.find_child_element(element, "LOWER-MULTIPLICITY")
        if child is not None:
            lower_multiplicity_value = child.text
            obj.lower_multiplicity = lower_multiplicity_value

        # Parse related_trace_ref
        child = SerializationHelper.find_child_element(element, "RELATED-TRACE-REF")
        if child is not None:
            related_trace_ref_value = ARRef.deserialize(child)
            obj.related_trace_ref = related_trace_ref_value

        # Parse scope
        child = SerializationHelper.find_child_element(element, "SCOPE")
        if child is not None:
            scope_value = EcucScopeEnum.deserialize(child)
            obj.scope = scope_value

        # Parse upper_multiplicity
        child = SerializationHelper.find_child_element(element, "UPPER-MULTIPLICITY")
        if child is not None:
            upper_multiplicity_value = child.text
            obj.upper_multiplicity = upper_multiplicity_value

        return obj



class EcucDefinitionElementBuilder(IdentifiableBuilder):
    """Builder for EcucDefinitionElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDefinitionElement = EcucDefinitionElement()


    def with_ecuc_cond(self, value: Optional[any (EcucCondition)]) -> "EcucDefinitionElementBuilder":
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

    def with_ecuc_validations(self, items: list[EcucValidationCondition]) -> "EcucDefinitionElementBuilder":
        """Set ecuc_validations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = list(items) if items else []
        return self

    def with_lower_multiplicity(self, value: Optional[PositiveInteger]) -> "EcucDefinitionElementBuilder":
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

    def with_related_trace(self, value: Optional[Traceable]) -> "EcucDefinitionElementBuilder":
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

    def with_scope(self, value: Optional[EcucScopeEnum]) -> "EcucDefinitionElementBuilder":
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

    def with_upper_multiplicity(self, value: Optional[Boolean]) -> "EcucDefinitionElementBuilder":
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


    def add_ecuc_validation(self, item: EcucValidationCondition) -> "EcucDefinitionElementBuilder":
        """Add a single item to ecuc_validations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations.append(item)
        return self

    def clear_ecuc_validations(self) -> "EcucDefinitionElementBuilder":
        """Clear all items from ecuc_validations list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = []
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
    def build(self) -> EcucDefinitionElement:
        """Build and return the EcucDefinitionElement instance (abstract)."""
        raise NotImplementedError