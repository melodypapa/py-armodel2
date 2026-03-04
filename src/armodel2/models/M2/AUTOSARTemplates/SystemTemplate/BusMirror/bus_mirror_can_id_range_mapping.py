"""BusMirrorCanIdRangeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUS-MIRROR-CAN-ID-RANGE-MAPPING"


    destination_base: Optional[PositiveInteger]
    source_can_id_code: Optional[PositiveInteger]
    source_can_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-BASE": lambda obj, elem: setattr(obj, "destination_base", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOURCE-CAN-ID-CODE": lambda obj, elem: setattr(obj, "source_can_id_code", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOURCE-CAN-ID": lambda obj, elem: setattr(obj, "source_can_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorCanIdRangeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorCanIdRangeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_base
        if self.destination_base is not None:
            serialized = SerializationHelper.serialize_item(self.destination_base, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id_code
        if self.source_can_id_code is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id_code, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id
        if self.source_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdRangeMapping":
        """Deserialize XML element to BusMirrorCanIdRangeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdRangeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorCanIdRangeMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-BASE":
                setattr(obj, "destination_base", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOURCE-CAN-ID-CODE":
                setattr(obj, "source_can_id_code", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOURCE-CAN-ID":
                setattr(obj, "source_can_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class BusMirrorCanIdRangeMappingBuilder(BuilderBase):
    """Builder for BusMirrorCanIdRangeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()


    def with_destination_base(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set destination_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_base = value
        return self

    def with_source_can_id_code(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set source_can_id_code attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_can_id_code = value
        return self

    def with_source_can_id(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set source_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_can_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "destinationBase",
        "sourceCanId",
        "sourceCanIdCode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return the BusMirrorCanIdRangeMapping instance with validation."""
        self._validate_instance()
        return self._obj