"""IEEE1722TpRvfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 649)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import IEEE1722TpAvConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfColorSpaceEnum,
    IEEE1722TpRvfFrameRateEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpRvfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-RVF-CONNECTION"


    rvf_active_pixels: Optional[PositiveInteger]
    rvf_color_space: Optional[IEEE1722TpRvfColorSpaceEnum]
    rvf_event_default: Optional[PositiveInteger]
    rvf_frame_rate: Optional[IEEE1722TpRvfFrameRateEnum]
    rvf_interlaced: Optional[Boolean]
    rvf_pixel_depth: Optional[Any]
    rvf_pixel_format: Optional[Any]
    rvf_total_lines: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "RVF-ACTIVE-PIXELS": lambda obj, elem: setattr(obj, "rvf_active_pixels", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RVF-COLOR-SPACE": lambda obj, elem: setattr(obj, "rvf_color_space", IEEE1722TpRvfColorSpaceEnum.deserialize(elem)),
        "RVF-EVENT-DEFAULT": lambda obj, elem: setattr(obj, "rvf_event_default", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RVF-FRAME-RATE": lambda obj, elem: setattr(obj, "rvf_frame_rate", IEEE1722TpRvfFrameRateEnum.deserialize(elem)),
        "RVF-INTERLACED": lambda obj, elem: setattr(obj, "rvf_interlaced", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RVF-PIXEL-DEPTH": lambda obj, elem: setattr(obj, "rvf_pixel_depth", SerializationHelper.deserialize_by_tag(elem, "any (IEEE1722TpRvfPixel)")),
        "RVF-PIXEL-FORMAT": lambda obj, elem: setattr(obj, "rvf_pixel_format", SerializationHelper.deserialize_by_tag(elem, "any (IEEE1722TpRvfPixel)")),
        "RVF-TOTAL-LINES": lambda obj, elem: setattr(obj, "rvf_total_lines", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpRvfConnection."""
        super().__init__()
        self.rvf_active_pixels: Optional[PositiveInteger] = None
        self.rvf_color_space: Optional[IEEE1722TpRvfColorSpaceEnum] = None
        self.rvf_event_default: Optional[PositiveInteger] = None
        self.rvf_frame_rate: Optional[IEEE1722TpRvfFrameRateEnum] = None
        self.rvf_interlaced: Optional[Boolean] = None
        self.rvf_pixel_depth: Optional[Any] = None
        self.rvf_pixel_format: Optional[Any] = None
        self.rvf_total_lines: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpRvfConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpRvfConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rvf_active_pixels
        if self.rvf_active_pixels is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_active_pixels, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-ACTIVE-PIXELS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_color_space
        if self.rvf_color_space is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_color_space, "IEEE1722TpRvfColorSpaceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-COLOR-SPACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_event_default
        if self.rvf_event_default is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_event_default, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-EVENT-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_frame_rate
        if self.rvf_frame_rate is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_frame_rate, "IEEE1722TpRvfFrameRateEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-FRAME-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_interlaced
        if self.rvf_interlaced is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_interlaced, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-INTERLACED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_pixel_depth
        if self.rvf_pixel_depth is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_pixel_depth, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-PIXEL-DEPTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_pixel_format
        if self.rvf_pixel_format is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_pixel_format, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-PIXEL-FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_total_lines
        if self.rvf_total_lines is not None:
            serialized = SerializationHelper.serialize_item(self.rvf_total_lines, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-TOTAL-LINES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpRvfConnection":
        """Deserialize XML element to IEEE1722TpRvfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpRvfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpRvfConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RVF-ACTIVE-PIXELS":
                setattr(obj, "rvf_active_pixels", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RVF-COLOR-SPACE":
                setattr(obj, "rvf_color_space", IEEE1722TpRvfColorSpaceEnum.deserialize(child))
            elif tag == "RVF-EVENT-DEFAULT":
                setattr(obj, "rvf_event_default", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RVF-FRAME-RATE":
                setattr(obj, "rvf_frame_rate", IEEE1722TpRvfFrameRateEnum.deserialize(child))
            elif tag == "RVF-INTERLACED":
                setattr(obj, "rvf_interlaced", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RVF-PIXEL-DEPTH":
                setattr(obj, "rvf_pixel_depth", SerializationHelper.deserialize_by_tag(child, "any (IEEE1722TpRvfPixel)"))
            elif tag == "RVF-PIXEL-FORMAT":
                setattr(obj, "rvf_pixel_format", SerializationHelper.deserialize_by_tag(child, "any (IEEE1722TpRvfPixel)"))
            elif tag == "RVF-TOTAL-LINES":
                setattr(obj, "rvf_total_lines", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpRvfConnectionBuilder(IEEE1722TpAvConnectionBuilder):
    """Builder for IEEE1722TpRvfConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpRvfConnection = IEEE1722TpRvfConnection()


    def with_rvf_active_pixels(self, value: Optional[PositiveInteger]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_active_pixels attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_active_pixels = value
        return self

    def with_rvf_color_space(self, value: Optional[IEEE1722TpRvfColorSpaceEnum]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_color_space attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_color_space = value
        return self

    def with_rvf_event_default(self, value: Optional[PositiveInteger]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_event_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_event_default = value
        return self

    def with_rvf_frame_rate(self, value: Optional[IEEE1722TpRvfFrameRateEnum]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_frame_rate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_frame_rate = value
        return self

    def with_rvf_interlaced(self, value: Optional[Boolean]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_interlaced attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_interlaced = value
        return self

    def with_rvf_pixel_depth(self, value: Optional[any (IEEE1722TpRvfPixel)]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_pixel_depth attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_pixel_depth = value
        return self

    def with_rvf_pixel_format(self, value: Optional[any (IEEE1722TpRvfPixel)]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_pixel_format attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_pixel_format = value
        return self

    def with_rvf_total_lines(self, value: Optional[PositiveInteger]) -> "IEEE1722TpRvfConnectionBuilder":
        """Set rvf_total_lines attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rvf_total_lines = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> IEEE1722TpRvfConnection:
        """Build and return the IEEE1722TpRvfConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj