"""GlobalTimeCorrectionProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 862)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeCorrectionProps(ARObject):
    """AUTOSAR GlobalTimeCorrectionProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-CORRECTION-PROPS"


    offset_correction: Optional[TimeValue]
    rate_correction: Optional[TimeValue]
    rate_corrections: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "OFFSET-CORRECTION": lambda obj, elem: setattr(obj, "offset_correction", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "RATE-CORRECTION": lambda obj, elem: setattr(obj, "rate_correction", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "RATE-CORRECTIONS": lambda obj, elem: setattr(obj, "rate_corrections", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeCorrectionProps."""
        super().__init__()
        self.offset_correction: Optional[TimeValue] = None
        self.rate_correction: Optional[TimeValue] = None
        self.rate_corrections: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCorrectionProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCorrectionProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize offset_correction
        if self.offset_correction is not None:
            serialized = SerializationHelper.serialize_item(self.offset_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_correction
        if self.rate_correction is not None:
            serialized = SerializationHelper.serialize_item(self.rate_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_corrections
        if self.rate_corrections is not None:
            serialized = SerializationHelper.serialize_item(self.rate_corrections, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCorrectionProps":
        """Deserialize XML element to GlobalTimeCorrectionProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCorrectionProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCorrectionProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OFFSET-CORRECTION":
                setattr(obj, "offset_correction", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "RATE-CORRECTION":
                setattr(obj, "rate_correction", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "RATE-CORRECTIONS":
                setattr(obj, "rate_corrections", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class GlobalTimeCorrectionPropsBuilder(BuilderBase):
    """Builder for GlobalTimeCorrectionProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeCorrectionProps = GlobalTimeCorrectionProps()


    def with_offset_correction(self, value: Optional[TimeValue]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set offset_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'offset_correction' is required and cannot be None")
        self._obj.offset_correction = value
        return self

    def with_rate_correction(self, value: Optional[TimeValue]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set rate_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rate_correction' is required and cannot be None")
        self._obj.rate_correction = value
        return self

    def with_rate_corrections(self, value: Optional[PositiveInteger]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set rate_corrections attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rate_corrections' is required and cannot be None")
        self._obj.rate_corrections = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "offsetCorrection",
        "rateCorrection",
        "rateCorrections",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GlobalTimeCorrectionProps:
        """Build and return the GlobalTimeCorrectionProps instance with validation."""
        self._validate_instance()
        return self._obj