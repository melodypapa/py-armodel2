"""TransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 772)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TransformationISignalProps(ARObject, ABC):
    """AUTOSAR TransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cs_error_reaction: Optional[CSTransformerErrorReactionEnum]
    data_prototype_refs: list[ARRef]
    transformer_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototype_refs: list[ARRef] = []
        self.transformer_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformationISignalProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize cs_error_reaction
        if self.cs_error_reaction is not None:
            serialized = SerializationHelper.serialize_item(self.cs_error_reaction, "CSTransformerErrorReactionEnum")
            if serialized is not None:
                wrapped = ET.Element("CS-ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize data_prototype_refs (list from container "DATA-PROTOTYPE-REFS")
        if self.data_prototype_refs:
            container = ET.Element("DATA-PROTOTYPE-REFS")
            for item in self.data_prototype_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("DataPrototype", package_data):
                    # Simple primitive type
                    child = ET.Element("DATA-PROTOTYPE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("DataPrototype", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize transformer_ref
        if self.transformer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transformer_ref, "Any")
            if serialized is not None:
                wrapped = ET.Element("TRANSFORMER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationISignalProps":
        """Deserialize XML element to TransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationISignalProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformationISignalProps, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse cs_error_reaction
        child = SerializationHelper.find_child_element(inner_elem, "CS-ERROR-REACTION")
        if child is not None:
            cs_error_reaction_value = CSTransformerErrorReactionEnum.deserialize(child)
            obj.cs_error_reaction = cs_error_reaction_value

        # Parse data_prototype_refs (list from container "DATA-PROTOTYPE-REFS")
        obj.data_prototype_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "DATA-PROTOTYPE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("DataPrototype", package_data):
                    child_value = child.text
                elif is_enum_type("DataPrototype", package_data):
                    child_value = DataPrototype.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_prototype_refs.append(child_value)

        # Parse transformer_ref
        child = SerializationHelper.find_child_element(inner_elem, "TRANSFORMER-REF")
        if child is not None:
            transformer_ref_value = ARRef.deserialize(child)
            obj.transformer_ref = transformer_ref_value

        return obj



class TransformationISignalPropsBuilder(BuilderBase, ABC):
    """Builder for TransformationISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransformationISignalProps = TransformationISignalProps()


    def with_cs_error_reaction(self, value: Optional[CSTransformerErrorReactionEnum]) -> "TransformationISignalPropsBuilder":
        """Set cs_error_reaction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cs_error_reaction = value
        return self

    def with_data_prototypes(self, items: list[DataPrototype]) -> "TransformationISignalPropsBuilder":
        """Set data_prototypes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_prototypes = list(items) if items else []
        return self

    def with_transformer(self, value: Optional[any (Transformation)]) -> "TransformationISignalPropsBuilder":
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


    def add_data_prototype(self, item: DataPrototype) -> "TransformationISignalPropsBuilder":
        """Add a single item to data_prototypes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_prototypes.append(item)
        return self

    def clear_data_prototypes(self) -> "TransformationISignalPropsBuilder":
        """Clear all items from data_prototypes list.

        Returns:
            self for method chaining
        """
        self._obj.data_prototypes = []
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
    def build(self) -> TransformationISignalProps:
        """Build and return the TransformationISignalProps instance (abstract)."""
        raise NotImplementedError