"""RxIdentifierRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RxIdentifierRange(ARObject):
    """AUTOSAR RxIdentifierRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RX-IDENTIFIER-RANGE"


    lower_can_id: Optional[PositiveInteger]
    upper_can_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "LOWER-CAN-ID": lambda obj, elem: setattr(obj, "lower_can_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "UPPER-CAN-ID": lambda obj, elem: setattr(obj, "upper_can_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize RxIdentifierRange."""
        super().__init__()
        self.lower_can_id: Optional[PositiveInteger] = None
        self.upper_can_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize RxIdentifierRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RxIdentifierRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_can_id
        if self.lower_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.lower_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_can_id
        if self.upper_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.upper_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RxIdentifierRange":
        """Deserialize XML element to RxIdentifierRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RxIdentifierRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RxIdentifierRange, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LOWER-CAN-ID":
                setattr(obj, "lower_can_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "UPPER-CAN-ID":
                setattr(obj, "upper_can_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class RxIdentifierRangeBuilder(BuilderBase):
    """Builder for RxIdentifierRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RxIdentifierRange = RxIdentifierRange()


    def with_lower_can_id(self, value: Optional[PositiveInteger]) -> "RxIdentifierRangeBuilder":
        """Set lower_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lower_can_id = value
        return self

    def with_upper_can_id(self, value: Optional[PositiveInteger]) -> "RxIdentifierRangeBuilder":
        """Set upper_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_can_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "lowerCanId",
        "upperCanId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RxIdentifierRange:
        """Build and return the RxIdentifierRange instance with validation."""
        self._validate_instance()
        return self._obj