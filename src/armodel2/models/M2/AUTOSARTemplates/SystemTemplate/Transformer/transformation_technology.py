"""TransformationTechnology AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 764)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformerClassEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.buffer_properties import (
    BufferProperties,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransformationTechnology(Identifiable):
    """AUTOSAR TransformationTechnology."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSFORMATION-TECHNOLOGY"


    buffer_properties: Optional[BufferProperties]
    has_internal: Optional[Boolean]
    needs_original: Optional[Boolean]
    protocol: Optional[String]
    transformation_description: Optional[TransformationDescription]
    transformer: Optional[TransformerClassEnum]
    version: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "BUFFER-PROPERTIES": lambda obj, elem: setattr(obj, "buffer_properties", BufferProperties.deserialize(elem)),
        "HAS-INTERNAL": lambda obj, elem: setattr(obj, "has_internal", elem.text),
        "NEEDS-ORIGINAL": lambda obj, elem: setattr(obj, "needs_original", elem.text),
        "PROTOCOL": lambda obj, elem: setattr(obj, "protocol", elem.text),
        "TRANSFORMATION-DESCRIPTION": lambda obj, elem: setattr(obj, "transformation_description", TransformationDescription.deserialize(elem)),
        "TRANSFORMER": lambda obj, elem: setattr(obj, "transformer", TransformerClassEnum.deserialize(elem)),
        "VERSION": lambda obj, elem: setattr(obj, "version", elem.text),
    }


    def __init__(self) -> None:
        """Initialize TransformationTechnology."""
        super().__init__()
        self.buffer_properties: Optional[BufferProperties] = None
        self.has_internal: Optional[Boolean] = None
        self.needs_original: Optional[Boolean] = None
        self.protocol: Optional[String] = None
        self.transformation_description: Optional[TransformationDescription] = None
        self.transformer: Optional[TransformerClassEnum] = None
        self.version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize TransformationTechnology to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformationTechnology, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize buffer_properties
        if self.buffer_properties is not None:
            serialized = SerializationHelper.serialize_item(self.buffer_properties, "BufferProperties")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUFFER-PROPERTIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_internal
        if self.has_internal is not None:
            serialized = SerializationHelper.serialize_item(self.has_internal, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-INTERNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize needs_original
        if self.needs_original is not None:
            serialized = SerializationHelper.serialize_item(self.needs_original, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEEDS-ORIGINAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize protocol
        if self.protocol is not None:
            serialized = SerializationHelper.serialize_item(self.protocol, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_description
        if self.transformation_description is not None:
            serialized = SerializationHelper.serialize_item(self.transformation_description, "TransformationDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMATION-DESCRIPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformer
        if self.transformer is not None:
            serialized = SerializationHelper.serialize_item(self.transformer, "TransformerClassEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version
        if self.version is not None:
            serialized = SerializationHelper.serialize_item(self.version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationTechnology":
        """Deserialize XML element to TransformationTechnology object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationTechnology object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformationTechnology, cls).deserialize(element)

        # Parse buffer_properties
        child = SerializationHelper.find_child_element(element, "BUFFER-PROPERTIES")
        if child is not None:
            buffer_properties_value = SerializationHelper.deserialize_by_tag(child, "BufferProperties")
            obj.buffer_properties = buffer_properties_value

        # Parse has_internal
        child = SerializationHelper.find_child_element(element, "HAS-INTERNAL")
        if child is not None:
            has_internal_value = child.text
            obj.has_internal = has_internal_value

        # Parse needs_original
        child = SerializationHelper.find_child_element(element, "NEEDS-ORIGINAL")
        if child is not None:
            needs_original_value = child.text
            obj.needs_original = needs_original_value

        # Parse protocol
        child = SerializationHelper.find_child_element(element, "PROTOCOL")
        if child is not None:
            protocol_value = child.text
            obj.protocol = protocol_value

        # Parse transformation_description
        child = SerializationHelper.find_child_element(element, "TRANSFORMATION-DESCRIPTION")
        if child is not None:
            transformation_description_value = SerializationHelper.deserialize_by_tag(child, "TransformationDescription")
            obj.transformation_description = transformation_description_value

        # Parse transformer
        child = SerializationHelper.find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = TransformerClassEnum.deserialize(child)
            obj.transformer = transformer_value

        # Parse version
        child = SerializationHelper.find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        return obj



class TransformationTechnologyBuilder(IdentifiableBuilder):
    """Builder for TransformationTechnology with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransformationTechnology = TransformationTechnology()


    def with_buffer_properties(self, value: Optional[BufferProperties]) -> "TransformationTechnologyBuilder":
        """Set buffer_properties attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.buffer_properties = value
        return self

    def with_has_internal(self, value: Optional[Boolean]) -> "TransformationTechnologyBuilder":
        """Set has_internal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.has_internal = value
        return self

    def with_needs_original(self, value: Optional[Boolean]) -> "TransformationTechnologyBuilder":
        """Set needs_original attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.needs_original = value
        return self

    def with_protocol(self, value: Optional[String]) -> "TransformationTechnologyBuilder":
        """Set protocol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol = value
        return self

    def with_transformation_description(self, value: Optional[TransformationDescription]) -> "TransformationTechnologyBuilder":
        """Set transformation_description attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transformation_description = value
        return self

    def with_transformer(self, value: Optional[TransformerClassEnum]) -> "TransformationTechnologyBuilder":
        """Set transformer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transformer = value
        return self

    def with_version(self, value: Optional[String]) -> "TransformationTechnologyBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version = value
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


    def build(self) -> TransformationTechnology:
        """Build and return the TransformationTechnology instance with validation."""
        self._validate_instance()
        pass
        return self._obj