"""Sdf AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 92)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Numerical,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Sdf(ARObject):
    """AUTOSAR Sdf."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDF"


    gid: NameToken
    value: Optional[Numerical]
    _DESERIALIZE_DISPATCH = {
        "GID": lambda obj, elem: setattr(obj, "gid", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
    }


    def __init__(self) -> None:
        """Initialize Sdf."""
        super().__init__()
        self.gid: NameToken = None
        self.value: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize Sdf to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Sdf, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize gid
        if self.gid is not None:
            serialized = SerializationHelper.serialize_item(self.gid, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdf":
        """Deserialize XML element to Sdf object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sdf object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Sdf, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "GID":
                setattr(obj, "gid", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "Numerical"))

        return obj



class SdfBuilder(BuilderBase):
    """Builder for Sdf with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Sdf = Sdf()


    def with_gid(self, value: NameToken) -> "SdfBuilder":
        """Set gid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.gid = value
        return self

    def with_value(self, value: Optional[Numerical]) -> "SdfBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "gid",
    }
    _OPTIONAL_ATTRIBUTES = {
        "value",
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
        if getattr(self._obj, "gid", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'gid' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'gid' is None", UserWarning)


    def build(self) -> Sdf:
        """Build and return the Sdf instance with validation."""
        self._validate_instance()
        return self._obj