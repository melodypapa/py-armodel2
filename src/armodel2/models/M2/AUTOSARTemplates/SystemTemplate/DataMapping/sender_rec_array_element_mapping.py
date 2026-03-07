"""SenderRecArrayElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
    IndexedArrayElement,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderRecArrayElementMapping(ARObject):
    """AUTOSAR SenderRecArrayElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENDER-REC-ARRAY-ELEMENT-MAPPING"


    complex_type: Optional[SenderRecCompositeTypeMapping]
    indexed_array: Optional[IndexedArrayElement]
    system_signal_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMPLEX-TYPE": ("_POLYMORPHIC", "complex_type", ["SenderRecArrayTypeMapping", "SenderRecRecordTypeMapping"]),
        "INDEXED-ARRAY": lambda obj, elem: setattr(obj, "indexed_array", SerializationHelper.deserialize_by_tag(elem, "IndexedArrayElement")),
        "SYSTEM-SIGNAL-REF": lambda obj, elem: setattr(obj, "system_signal_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SenderRecArrayElementMapping."""
        super().__init__()
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.indexed_array: Optional[IndexedArrayElement] = None
        self.system_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderRecArrayElementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecArrayElementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize complex_type
        if self.complex_type is not None:
            serialized = SerializationHelper.serialize_item(self.complex_type, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPLEX-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indexed_array
        if self.indexed_array is not None:
            serialized = SerializationHelper.serialize_item(self.indexed_array, "IndexedArrayElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEXED-ARRAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_ref
        if self.system_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayElementMapping":
        """Deserialize XML element to SenderRecArrayElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayElementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecArrayElementMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPLEX-TYPE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "SENDER-REC-ARRAY-TYPE-MAPPING":
                        setattr(obj, "complex_type", SerializationHelper.deserialize_by_tag(child[0], "SenderRecArrayTypeMapping"))
                    elif concrete_tag == "SENDER-REC-RECORD-TYPE-MAPPING":
                        setattr(obj, "complex_type", SerializationHelper.deserialize_by_tag(child[0], "SenderRecRecordTypeMapping"))
            elif tag == "INDEXED-ARRAY":
                setattr(obj, "indexed_array", SerializationHelper.deserialize_by_tag(child, "IndexedArrayElement"))
            elif tag == "SYSTEM-SIGNAL-REF":
                setattr(obj, "system_signal_ref", ARRef.deserialize(child))

        return obj



class SenderRecArrayElementMappingBuilder(BuilderBase):
    """Builder for SenderRecArrayElementMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderRecArrayElementMapping = SenderRecArrayElementMapping()


    def with_complex_type(self, value: Optional[SenderRecCompositeTypeMapping]) -> "SenderRecArrayElementMappingBuilder":
        """Set complex_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'complex_type' is required and cannot be None")
        self._obj.complex_type = value
        return self

    def with_indexed_array(self, value: Optional[IndexedArrayElement]) -> "SenderRecArrayElementMappingBuilder":
        """Set indexed_array attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'indexed_array' is required and cannot be None")
        self._obj.indexed_array = value
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> "SenderRecArrayElementMappingBuilder":
        """Set system_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'system_signal' is required and cannot be None")
        self._obj.system_signal = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "complexType",
        "indexedArray",
        "systemSignal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SenderRecArrayElementMapping:
        """Build and return the SenderRecArrayElementMapping instance with validation."""
        self._validate_instance()
        return self._obj