"""DataTransformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 763)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataTransformation(Identifiable):
    """AUTOSAR DataTransformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-TRANSFORMATION"


    data: Optional[DataTransformationKindEnum]
    execute_despite: Optional[Boolean]
    transformer_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "DATA": lambda obj, elem: setattr(obj, "data", DataTransformationKindEnum.deserialize(elem)),
        "EXECUTE-DESPITE": lambda obj, elem: setattr(obj, "execute_despite", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TRANSFORMERS": lambda obj, elem: obj.transformer_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DataTransformation."""
        super().__init__()
        self.data: Optional[DataTransformationKindEnum] = None
        self.execute_despite: Optional[Boolean] = None
        self.transformer_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DataTransformation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTransformation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data
        if self.data is not None:
            serialized = SerializationHelper.serialize_item(self.data, "DataTransformationKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execute_despite
        if self.execute_despite is not None:
            serialized = SerializationHelper.serialize_item(self.execute_despite, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTE-DESPITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformer_refs (list to container "TRANSFORMER-REFS")
        if self.transformer_refs:
            wrapper = ET.Element("TRANSFORMER-REFS")
            for item in self.transformer_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("TRANSFORMER-REF")
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
    def deserialize(cls, element: ET.Element) -> "DataTransformation":
        """Deserialize XML element to DataTransformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTransformation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA":
                setattr(obj, "data", DataTransformationKindEnum.deserialize(child))
            elif tag == "EXECUTE-DESPITE":
                setattr(obj, "execute_despite", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TRANSFORMERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.transformer_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (Transformation)"))

        return obj



class DataTransformationBuilder(IdentifiableBuilder):
    """Builder for DataTransformation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataTransformation = DataTransformation()


    def with_data(self, value: Optional[DataTransformationKindEnum]) -> "DataTransformationBuilder":
        """Set data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data = value
        return self

    def with_execute_despite(self, value: Optional[Boolean]) -> "DataTransformationBuilder":
        """Set execute_despite attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.execute_despite = value
        return self

    def with_transformers(self, items: list[any (Transformation)]) -> "DataTransformationBuilder":
        """Set transformers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformers = list(items) if items else []
        return self


    def add_transformer(self, item: any (Transformation)) -> "DataTransformationBuilder":
        """Add a single item to transformers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformers.append(item)
        return self

    def clear_transformers(self) -> "DataTransformationBuilder":
        """Clear all items from transformers list.

        Returns:
            self for method chaining
        """
        self._obj.transformers = []
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


    def build(self) -> DataTransformation:
        """Build and return the DataTransformation instance with validation."""
        self._validate_instance()
        pass
        return self._obj