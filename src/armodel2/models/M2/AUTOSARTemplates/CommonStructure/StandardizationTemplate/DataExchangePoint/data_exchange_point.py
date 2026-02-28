"""DataExchangePoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.baseline import (
    Baseline,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_tailoring import (
    DataFormatTailoring,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_scope import (
    SpecificationScope,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataExchangePoint(ARElement):
    """AUTOSAR DataExchangePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-EXCHANGE-POINT"


    data_format: Optional[DataFormatTailoring]
    kind: DataExchangePoint
    referenced: Baseline
    specification_scope: Optional[SpecificationScope]
    _DESERIALIZE_DISPATCH = {
        "DATA-FORMAT": lambda obj, elem: setattr(obj, "data_format", DataFormatTailoring.deserialize(elem)),
        "KIND": lambda obj, elem: setattr(obj, "kind", DataExchangePoint.deserialize(elem)),
        "REFERENCED": lambda obj, elem: setattr(obj, "referenced", Baseline.deserialize(elem)),
        "SPECIFICATION-SCOPE": lambda obj, elem: setattr(obj, "specification_scope", SpecificationScope.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DataExchangePoint."""
        super().__init__()
        self.data_format: Optional[DataFormatTailoring] = None
        self.kind: DataExchangePoint = None
        self.referenced: Baseline = None
        self.specification_scope: Optional[SpecificationScope] = None

    def serialize(self) -> ET.Element:
        """Serialize DataExchangePoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataExchangePoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_format
        if self.data_format is not None:
            serialized = SerializationHelper.serialize_item(self.data_format, "DataFormatTailoring")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize kind
        if self.kind is not None:
            serialized = SerializationHelper.serialize_item(self.kind, "DataExchangePoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referenced
        if self.referenced is not None:
            serialized = SerializationHelper.serialize_item(self.referenced, "Baseline")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize specification_scope
        if self.specification_scope is not None:
            serialized = SerializationHelper.serialize_item(self.specification_scope, "SpecificationScope")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPECIFICATION-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataExchangePoint":
        """Deserialize XML element to DataExchangePoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataExchangePoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataExchangePoint, cls).deserialize(element)

        # Parse data_format
        child = SerializationHelper.find_child_element(element, "DATA-FORMAT")
        if child is not None:
            data_format_value = SerializationHelper.deserialize_by_tag(child, "DataFormatTailoring")
            obj.data_format = data_format_value

        # Parse kind
        child = SerializationHelper.find_child_element(element, "KIND")
        if child is not None:
            kind_value = SerializationHelper.deserialize_by_tag(child, "DataExchangePoint")
            obj.kind = kind_value

        # Parse referenced
        child = SerializationHelper.find_child_element(element, "REFERENCED")
        if child is not None:
            referenced_value = SerializationHelper.deserialize_by_tag(child, "Baseline")
            obj.referenced = referenced_value

        # Parse specification_scope
        child = SerializationHelper.find_child_element(element, "SPECIFICATION-SCOPE")
        if child is not None:
            specification_scope_value = SerializationHelper.deserialize_by_tag(child, "SpecificationScope")
            obj.specification_scope = specification_scope_value

        return obj



class DataExchangePointBuilder(ARElementBuilder):
    """Builder for DataExchangePoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataExchangePoint = DataExchangePoint()


    def with_data_format(self, value: Optional[DataFormatTailoring]) -> "DataExchangePointBuilder":
        """Set data_format attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_format = value
        return self

    def with_kind(self, value: DataExchangePoint) -> "DataExchangePointBuilder":
        """Set kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.kind = value
        return self

    def with_referenced(self, value: Baseline) -> "DataExchangePointBuilder":
        """Set referenced attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.referenced = value
        return self

    def with_specification_scope(self, value: Optional[SpecificationScope]) -> "DataExchangePointBuilder":
        """Set specification_scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.specification_scope = value
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


    def build(self) -> DataExchangePoint:
        """Build and return the DataExchangePoint instance with validation."""
        self._validate_instance()
        pass
        return self._obj