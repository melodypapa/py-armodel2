"""LimitValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    IntervalTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LimitValueVariationPoint(ARObject):
    """AUTOSAR LimitValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIMIT-VALUE-VARIATION-POINT"


    interval_type_enum: Optional[IntervalTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "INTERVAL-TYPE-ENUM": lambda obj, elem: setattr(obj, "interval_type_enum", IntervalTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LimitValueVariationPoint."""
        super().__init__()
        self.interval_type_enum: Optional[IntervalTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize LimitValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LimitValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interval_type_enum
        if self.interval_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.interval_type_enum, "IntervalTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERVAL-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LimitValueVariationPoint":
        """Deserialize XML element to LimitValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LimitValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LimitValueVariationPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERVAL-TYPE-ENUM":
                setattr(obj, "interval_type_enum", IntervalTypeEnum.deserialize(child))

        return obj



class LimitValueVariationPointBuilder(BuilderBase):
    """Builder for LimitValueVariationPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LimitValueVariationPoint = LimitValueVariationPoint()


    def with_interval_type_enum(self, value: Optional[IntervalTypeEnum]) -> "LimitValueVariationPointBuilder":
        """Set interval_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'interval_type_enum' is required and cannot be None")
        self._obj.interval_type_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "intervalTypeEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LimitValueVariationPoint:
        """Build and return the LimitValueVariationPoint instance with validation."""
        self._validate_instance()
        return self._obj