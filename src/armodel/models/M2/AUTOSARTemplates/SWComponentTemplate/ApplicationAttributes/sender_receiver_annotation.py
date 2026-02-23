"""SenderReceiverAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import GeneralAnnotationBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DataLimitKindEnum,
    ProcessingKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SenderReceiverAnnotation(GeneralAnnotation, ABC):
    """AUTOSAR SenderReceiverAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    computed: Optional[Boolean]
    data_element_ref: Optional[ARRef]
    limit_kind: Optional[DataLimitKindEnum]
    processing_kind_enum: Optional[ProcessingKindEnum]
    def __init__(self) -> None:
        """Initialize SenderReceiverAnnotation."""
        super().__init__()
        self.computed: Optional[Boolean] = None
        self.data_element_ref: Optional[ARRef] = None
        self.limit_kind: Optional[DataLimitKindEnum] = None
        self.processing_kind_enum: Optional[ProcessingKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize computed
        if self.computed is not None:
            serialized = SerializationHelper.serialize_item(self.computed, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPUTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize limit_kind
        if self.limit_kind is not None:
            serialized = SerializationHelper.serialize_item(self.limit_kind, "DataLimitKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIMIT-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_kind_enum
        if self.processing_kind_enum is not None:
            serialized = SerializationHelper.serialize_item(self.processing_kind_enum, "ProcessingKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-KIND-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverAnnotation":
        """Deserialize XML element to SenderReceiverAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverAnnotation, cls).deserialize(element)

        # Parse computed
        child = SerializationHelper.find_child_element(element, "COMPUTED")
        if child is not None:
            computed_value = child.text
            obj.computed = computed_value

        # Parse data_element_ref
        child = SerializationHelper.find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse limit_kind
        child = SerializationHelper.find_child_element(element, "LIMIT-KIND")
        if child is not None:
            limit_kind_value = DataLimitKindEnum.deserialize(child)
            obj.limit_kind = limit_kind_value

        # Parse processing_kind_enum
        child = SerializationHelper.find_child_element(element, "PROCESSING-KIND-ENUM")
        if child is not None:
            processing_kind_enum_value = ProcessingKindEnum.deserialize(child)
            obj.processing_kind_enum = processing_kind_enum_value

        return obj



class SenderReceiverAnnotationBuilder(GeneralAnnotationBuilder):
    """Builder for SenderReceiverAnnotation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderReceiverAnnotation = SenderReceiverAnnotation()


    def with_computed(self, value: Optional[Boolean]) -> "SenderReceiverAnnotationBuilder":
        """Set computed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.computed = value
        return self

    def with_data_element(self, value: Optional[VariableDataPrototype]) -> "SenderReceiverAnnotationBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_limit_kind(self, value: Optional[DataLimitKindEnum]) -> "SenderReceiverAnnotationBuilder":
        """Set limit_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.limit_kind = value
        return self

    def with_processing_kind_enum(self, value: Optional[ProcessingKindEnum]) -> "SenderReceiverAnnotationBuilder":
        """Set processing_kind_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processing_kind_enum = value
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


    @abstractmethod
    def build(self) -> SenderReceiverAnnotation:
        """Build and return the SenderReceiverAnnotation instance (abstract)."""
        raise NotImplementedError