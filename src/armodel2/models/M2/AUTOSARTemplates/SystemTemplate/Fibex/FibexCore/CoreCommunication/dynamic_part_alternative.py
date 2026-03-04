"""DynamicPartAlternative AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DYNAMIC-PART-ALTERNATIVE"


    initial_dynamic: Optional[Boolean]
    i_pdu_ref: Optional[ARRef]
    selector_field: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "INITIAL-DYNAMIC": lambda obj, elem: setattr(obj, "initial_dynamic", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "I-PDU-REF": lambda obj, elem: setattr(obj, "i_pdu_ref", ARRef.deserialize(elem)),
        "SELECTOR-FIELD": lambda obj, elem: setattr(obj, "selector_field", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu_ref: Optional[ARRef] = None
        self.selector_field: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DynamicPartAlternative to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DynamicPartAlternative, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_dynamic
        if self.initial_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.initial_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPartAlternative":
        """Deserialize XML element to DynamicPartAlternative object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DynamicPartAlternative object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DynamicPartAlternative, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INITIAL-DYNAMIC":
                setattr(obj, "initial_dynamic", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "I-PDU-REF":
                setattr(obj, "i_pdu_ref", ARRef.deserialize(child))
            elif tag == "SELECTOR-FIELD":
                setattr(obj, "selector_field", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class DynamicPartAlternativeBuilder(BuilderBase):
    """Builder for DynamicPartAlternative with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DynamicPartAlternative = DynamicPartAlternative()


    def with_initial_dynamic(self, value: Optional[Boolean]) -> "DynamicPartAlternativeBuilder":
        """Set initial_dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_dynamic = value
        return self

    def with_i_pdu(self, value: Optional[ISignalIPdu]) -> "DynamicPartAlternativeBuilder":
        """Set i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu = value
        return self

    def with_selector_field(self, value: Optional[Integer]) -> "DynamicPartAlternativeBuilder":
        """Set selector_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.selector_field = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iPdu",
        "initialDynamic",
        "selectorField",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DynamicPartAlternative:
        """Build and return the DynamicPartAlternative instance with validation."""
        self._validate_instance()
        return self._obj