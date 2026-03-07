"""MultiplexedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 408)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
    DynamicPart,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultiplexedIPdu(IPdu):
    """AUTOSAR MultiplexedIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MULTIPLEXED-I-PDU"


    dynamic_part: Optional[DynamicPart]
    selector_field: Optional[Integer]
    unused_bit: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "DYNAMIC-PART": lambda obj, elem: setattr(obj, "dynamic_part", SerializationHelper.deserialize_by_tag(elem, "DynamicPart")),
        "SELECTOR-FIELD": lambda obj, elem: setattr(obj, "selector_field", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "UNUSED-BIT": lambda obj, elem: setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize MultiplexedIPdu."""
        super().__init__()
        self.dynamic_part: Optional[DynamicPart] = None
        self.selector_field: Optional[Integer] = None
        self.unused_bit: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize MultiplexedIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiplexedIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_part
        if self.dynamic_part is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_part, "DynamicPart")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-PART")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize selector_field
        if self.selector_field is not None:
            serialized = SerializationHelper.serialize_item(self.selector_field, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECTOR-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = SerializationHelper.serialize_item(self.unused_bit, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedIPdu":
        """Deserialize XML element to MultiplexedIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiplexedIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiplexedIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DYNAMIC-PART":
                setattr(obj, "dynamic_part", SerializationHelper.deserialize_by_tag(child, "DynamicPart"))
            elif tag == "SELECTOR-FIELD":
                setattr(obj, "selector_field", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "UNUSED-BIT":
                setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class MultiplexedIPduBuilder(IPduBuilder):
    """Builder for MultiplexedIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultiplexedIPdu = MultiplexedIPdu()


    def with_dynamic_part(self, value: Optional[DynamicPart]) -> "MultiplexedIPduBuilder":
        """Set dynamic_part attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'dynamic_part' is required and cannot be None")
        self._obj.dynamic_part = value
        return self

    def with_selector_field(self, value: Optional[Integer]) -> "MultiplexedIPduBuilder":
        """Set selector_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'selector_field' is required and cannot be None")
        self._obj.selector_field = value
        return self

    def with_unused_bit(self, value: Optional[Integer]) -> "MultiplexedIPduBuilder":
        """Set unused_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'unused_bit' is required and cannot be None")
        self._obj.unused_bit = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dynamicPart",
        "selectorField",
        "unusedBit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MultiplexedIPdu:
        """Build and return the MultiplexedIPdu instance with validation."""
        self._validate_instance()
        return self._obj