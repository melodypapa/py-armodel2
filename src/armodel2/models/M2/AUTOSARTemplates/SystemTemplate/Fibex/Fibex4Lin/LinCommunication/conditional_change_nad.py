"""ConditionalChangeNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import LinConfigurationEntryBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONDITIONAL-CHANGE-NAD"


    byte: Optional[Integer]
    id: Optional[PositiveInteger]
    invert: Optional[Integer]
    mask: Optional[Integer]
    new_nad: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "BYTE": lambda obj, elem: setattr(obj, "byte", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "INVERT": lambda obj, elem: setattr(obj, "invert", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MASK": lambda obj, elem: setattr(obj, "mask", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NEW-NAD": lambda obj, elem: setattr(obj, "new_nad", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize ConditionalChangeNad to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConditionalChangeNad, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize byte
        if self.byte is not None:
            serialized = SerializationHelper.serialize_item(self.byte, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize invert
        if self.invert is not None:
            serialized = SerializationHelper.serialize_item(self.invert, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INVERT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = SerializationHelper.serialize_item(self.mask, "Integer")
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

        # Serialize new_nad
        if self.new_nad is not None:
            serialized = SerializationHelper.serialize_item(self.new_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEW-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionalChangeNad":
        """Deserialize XML element to ConditionalChangeNad object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConditionalChangeNad object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConditionalChangeNad, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BYTE":
                setattr(obj, "byte", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "INVERT":
                setattr(obj, "invert", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MASK":
                setattr(obj, "mask", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "NEW-NAD":
                setattr(obj, "new_nad", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class ConditionalChangeNadBuilder(LinConfigurationEntryBuilder):
    """Builder for ConditionalChangeNad with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConditionalChangeNad = ConditionalChangeNad()


    def with_byte(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set byte attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.byte = value
        return self

    def with_id(self, value: Optional[PositiveInteger]) -> "ConditionalChangeNadBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_invert(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set invert attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.invert = value
        return self

    def with_mask(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mask = value
        return self

    def with_new_nad(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set new_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.new_nad = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "byte",
        "id",
        "invert",
        "mask",
        "newNad",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConditionalChangeNad:
        """Build and return the ConditionalChangeNad instance with validation."""
        self._validate_instance()
        return self._obj