"""AbstractEnumerationValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)


class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[Identifier]
    enum_table_ref: Optional[Ref]
    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table_ref: Optional[Ref] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractEnumerationValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractEnumerationValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base
        if self.base is not None:
            serialized = SerializationHelper.serialize_item(self.base, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enum_table_ref
        if self.enum_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.enum_table_ref, "Ref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENUM-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEnumerationValueVariationPoint":
        """Deserialize XML element to AbstractEnumerationValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEnumerationValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractEnumerationValueVariationPoint, cls).deserialize(element)

        # Parse base
        child = SerializationHelper.find_child_element(element, "BASE")
        if child is not None:
            base_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.base = base_value

        # Parse enum_table_ref
        child = SerializationHelper.find_child_element(element, "ENUM-TABLE-REF")
        if child is not None:
            enum_table_ref_value = ARRef.deserialize(child)
            obj.enum_table_ref = enum_table_ref_value

        return obj



class AbstractEnumerationValueVariationPointBuilder(BuilderBase, ABC):
    """Builder for AbstractEnumerationValueVariationPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractEnumerationValueVariationPoint = AbstractEnumerationValueVariationPoint()


    def with_base(self, value: Optional[Identifier]) -> "AbstractEnumerationValueVariationPointBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_enum_table(self, value: Optional[Ref]) -> "AbstractEnumerationValueVariationPointBuilder":
        """Set enum_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enum_table = value
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
    def build(self) -> AbstractEnumerationValueVariationPoint:
        """Build and return the AbstractEnumerationValueVariationPoint instance (abstract)."""
        raise NotImplementedError