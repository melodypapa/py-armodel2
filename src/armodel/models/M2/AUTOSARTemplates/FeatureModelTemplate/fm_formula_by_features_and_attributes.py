"""FMFormulaByFeaturesAndAttributes AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFormulaByFeaturesAndAttributes(ARObject, ABC):
    """AUTOSAR FMFormulaByFeaturesAndAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute_ref: Optional[ARRef]
    feature_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndAttributes."""
        super().__init__()
        self.attribute_ref: Optional[ARRef] = None
        self.feature_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFormulaByFeaturesAndAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFormulaByFeaturesAndAttributes, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_ref
        if self.attribute_ref is not None:
            serialized = SerializationHelper.serialize_item(self.attribute_ref, "FMAttributeDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize feature_ref
        if self.feature_ref is not None:
            serialized = SerializationHelper.serialize_item(self.feature_ref, "FMFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndAttributes":
        """Deserialize XML element to FMFormulaByFeaturesAndAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFormulaByFeaturesAndAttributes object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFormulaByFeaturesAndAttributes, cls).deserialize(element)

        # Parse attribute_ref
        child = SerializationHelper.find_child_element(element, "ATTRIBUTE-REF")
        if child is not None:
            attribute_ref_value = ARRef.deserialize(child)
            obj.attribute_ref = attribute_ref_value

        # Parse feature_ref
        child = SerializationHelper.find_child_element(element, "FEATURE-REF")
        if child is not None:
            feature_ref_value = ARRef.deserialize(child)
            obj.feature_ref = feature_ref_value

        return obj



class FMFormulaByFeaturesAndAttributesBuilder(BuilderBase, ABC):
    """Builder for FMFormulaByFeaturesAndAttributes with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFormulaByFeaturesAndAttributes = FMFormulaByFeaturesAndAttributes()


    def with_attribute(self, value: Optional[FMAttributeDef]) -> "FMFormulaByFeaturesAndAttributesBuilder":
        """Set attribute attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.attribute = value
        return self

    def with_feature(self, value: Optional[FMFeature]) -> "FMFormulaByFeaturesAndAttributesBuilder":
        """Set feature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.feature = value
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
    def build(self) -> FMFormulaByFeaturesAndAttributes:
        """Build and return the FMFormulaByFeaturesAndAttributes instance (abstract)."""
        raise NotImplementedError