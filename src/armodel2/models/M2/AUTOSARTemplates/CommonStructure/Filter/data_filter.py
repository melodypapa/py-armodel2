"""DataFilter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 182)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 394)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Filter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter import (
    DataFilterTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    UnlimitedInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataFilter(ARObject):
    """AUTOSAR DataFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-FILTER"


    data_filter_type: Optional[DataFilterTypeEnum]
    mask: Optional[UnlimitedInteger]
    max: Optional[UnlimitedInteger]
    min: Optional[UnlimitedInteger]
    offset: Optional[PositiveInteger]
    period: Optional[PositiveInteger]
    x: Optional[UnlimitedInteger]
    _DESERIALIZE_DISPATCH = {
        "DATA-FILTER-TYPE": lambda obj, elem: setattr(obj, "data_filter_type", DataFilterTypeEnum.deserialize(elem)),
        "MASK": lambda obj, elem: setattr(obj, "mask", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
        "MAX": lambda obj, elem: setattr(obj, "max", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
        "MIN": lambda obj, elem: setattr(obj, "min", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
        "OFFSET": lambda obj, elem: setattr(obj, "offset", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PERIOD": lambda obj, elem: setattr(obj, "period", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "X": lambda obj, elem: setattr(obj, "x", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
    }


    def __init__(self) -> None:
        """Initialize DataFilter."""
        super().__init__()
        self.data_filter_type: Optional[DataFilterTypeEnum] = None
        self.mask: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.period: Optional[PositiveInteger] = None
        self.x: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DataFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_filter_type
        if self.data_filter_type is not None:
            serialized = SerializationHelper.serialize_item(self.data_filter_type, "DataFilterTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = SerializationHelper.serialize_item(self.mask, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = SerializationHelper.serialize_item(self.offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period
        if self.period is not None:
            serialized = SerializationHelper.serialize_item(self.period, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize x
        if self.x is not None:
            serialized = SerializationHelper.serialize_item(self.x, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("X")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFilter":
        """Deserialize XML element to DataFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataFilter, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-FILTER-TYPE":
                setattr(obj, "data_filter_type", DataFilterTypeEnum.deserialize(child))
            elif tag == "MASK":
                setattr(obj, "mask", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))
            elif tag == "MAX":
                setattr(obj, "max", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))
            elif tag == "MIN":
                setattr(obj, "min", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))
            elif tag == "OFFSET":
                setattr(obj, "offset", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PERIOD":
                setattr(obj, "period", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "X":
                setattr(obj, "x", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))

        return obj



class DataFilterBuilder(BuilderBase):
    """Builder for DataFilter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataFilter = DataFilter()


    def with_data_filter_type(self, value: Optional[DataFilterTypeEnum]) -> "DataFilterBuilder":
        """Set data_filter_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_filter_type' is required and cannot be None")
        self._obj.data_filter_type = value
        return self

    def with_mask(self, value: Optional[UnlimitedInteger]) -> "DataFilterBuilder":
        """Set mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mask' is required and cannot be None")
        self._obj.mask = value
        return self

    def with_max(self, value: Optional[UnlimitedInteger]) -> "DataFilterBuilder":
        """Set max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max' is required and cannot be None")
        self._obj.max = value
        return self

    def with_min(self, value: Optional[UnlimitedInteger]) -> "DataFilterBuilder":
        """Set min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min' is required and cannot be None")
        self._obj.min = value
        return self

    def with_offset(self, value: Optional[PositiveInteger]) -> "DataFilterBuilder":
        """Set offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'offset' is required and cannot be None")
        self._obj.offset = value
        return self

    def with_period(self, value: Optional[PositiveInteger]) -> "DataFilterBuilder":
        """Set period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'period' is required and cannot be None")
        self._obj.period = value
        return self

    def with_x(self, value: Optional[UnlimitedInteger]) -> "DataFilterBuilder":
        """Set x attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'x' is required and cannot be None")
        self._obj.x = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataFilterType",
        "mask",
        "max",
        "min",
        "offset",
        "period",
        "x",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataFilter:
        """Build and return the DataFilter instance with validation."""
        self._validate_instance()
        return self._obj