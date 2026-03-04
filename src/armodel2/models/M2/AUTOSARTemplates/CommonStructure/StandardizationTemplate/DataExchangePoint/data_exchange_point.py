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
        "DATA-FORMAT": lambda obj, elem: setattr(obj, "data_format", SerializationHelper.deserialize_by_tag(elem, "DataFormatTailoring")),
        "KIND": lambda obj, elem: setattr(obj, "kind", SerializationHelper.deserialize_by_tag(elem, "DataExchangePoint")),
        "REFERENCED": lambda obj, elem: setattr(obj, "referenced", SerializationHelper.deserialize_by_tag(elem, "Baseline")),
        "SPECIFICATION-SCOPE": lambda obj, elem: setattr(obj, "specification_scope", SerializationHelper.deserialize_by_tag(elem, "SpecificationScope")),
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-FORMAT":
                setattr(obj, "data_format", SerializationHelper.deserialize_by_tag(child, "DataFormatTailoring"))
            elif tag == "KIND":
                setattr(obj, "kind", SerializationHelper.deserialize_by_tag(child, "DataExchangePoint"))
            elif tag == "REFERENCED":
                setattr(obj, "referenced", SerializationHelper.deserialize_by_tag(child, "Baseline"))
            elif tag == "SPECIFICATION-SCOPE":
                setattr(obj, "specification_scope", SerializationHelper.deserialize_by_tag(child, "SpecificationScope"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "kind",
        "referenced",
    }
    _OPTIONAL_ATTRIBUTES = {
        "dataFormat",
        "specificationScope",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "kind", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'kind' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'kind' is None", UserWarning)
        if getattr(self._obj, "referenced", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'referenced' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'referenced' is None", UserWarning)


    def build(self) -> DataExchangePoint:
        """Build and return the DataExchangePoint instance with validation."""
        self._validate_instance()
        return self._obj