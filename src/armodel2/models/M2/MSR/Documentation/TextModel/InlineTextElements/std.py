"""Std AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import SingleLanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Std(SingleLanguageReferrable):
    """AUTOSAR Std."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STD"


    date: Optional[DateTime]
    position: Optional[String]
    state: Optional[String]
    subtitle: Optional[String]
    url: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DATE": lambda obj, elem: setattr(obj, "date", elem.text),
        "POSITION": lambda obj, elem: setattr(obj, "position", elem.text),
        "STATE": lambda obj, elem: setattr(obj, "state", elem.text),
        "SUBTITLE": lambda obj, elem: setattr(obj, "subtitle", elem.text),
        "URL": lambda obj, elem: setattr(obj, "url", any (Url).deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Std."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.position: Optional[String] = None
        self.state: Optional[String] = None
        self.subtitle: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize Std to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Std, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize date
        if self.date is not None:
            serialized = SerializationHelper.serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize position
        if self.position is not None:
            serialized = SerializationHelper.serialize_item(self.position, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = SerializationHelper.serialize_item(self.state, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subtitle
        if self.subtitle is not None:
            serialized = SerializationHelper.serialize_item(self.subtitle, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUBTITLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize url
        if self.url is not None:
            serialized = SerializationHelper.serialize_item(self.url, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("URL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Std":
        """Deserialize XML element to Std object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Std object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Std, cls).deserialize(element)

        # Parse date
        child = SerializationHelper.find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse position
        child = SerializationHelper.find_child_element(element, "POSITION")
        if child is not None:
            position_value = child.text
            obj.position = position_value

        # Parse state
        child = SerializationHelper.find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        # Parse subtitle
        child = SerializationHelper.find_child_element(element, "SUBTITLE")
        if child is not None:
            subtitle_value = child.text
            obj.subtitle = subtitle_value

        # Parse url
        child = SerializationHelper.find_child_element(element, "URL")
        if child is not None:
            url_value = child.text
            obj.url = url_value

        return obj



class StdBuilder(SingleLanguageReferrableBuilder):
    """Builder for Std with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Std = Std()


    def with_date(self, value: Optional[DateTime]) -> "StdBuilder":
        """Set date attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.date = value
        return self

    def with_position(self, value: Optional[String]) -> "StdBuilder":
        """Set position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.position = value
        return self

    def with_state(self, value: Optional[String]) -> "StdBuilder":
        """Set state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.state = value
        return self

    def with_subtitle(self, value: Optional[String]) -> "StdBuilder":
        """Set subtitle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.subtitle = value
        return self

    def with_url(self, value: Optional[any (Url)]) -> "StdBuilder":
        """Set url attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.url = value
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


    def build(self) -> Std:
        """Build and return the Std instance with validation."""
        self._validate_instance()
        pass
        return self._obj