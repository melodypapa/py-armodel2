"""EmphasisText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 316)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    EEnum,
    EEnumFont,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class EmphasisText(ARObject):
    """AUTOSAR EmphasisText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    color: Optional[String]
    font: Optional[EEnumFont]
    sub: Superscript
    sup: Superscript
    tt: Optional[Tt]
    type: Optional[EEnum]
    def __init__(self) -> None:
        """Initialize EmphasisText."""
        super().__init__()
        self.color: Optional[String] = None
        self.font: Optional[EEnumFont] = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Optional[Tt] = None
        self.type: Optional[EEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize EmphasisText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EmphasisText, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize color
        if self.color is not None:
            serialized = SerializationHelper.serialize_item(self.color, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize font
        if self.font is not None:
            serialized = SerializationHelper.serialize_item(self.font, "EEnumFont")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FONT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub
        if self.sub is not None:
            serialized = SerializationHelper.serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = SerializationHelper.serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tt
        if self.tt is not None:
            serialized = SerializationHelper.serialize_item(self.tt, "Tt")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type
        if self.type is not None:
            serialized = SerializationHelper.serialize_item(self.type, "EEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EmphasisText":
        """Deserialize XML element to EmphasisText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EmphasisText object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EmphasisText, cls).deserialize(element)

        # Parse color
        child = SerializationHelper.find_child_element(element, "COLOR")
        if child is not None:
            color_value = child.text
            obj.color = color_value

        # Parse font
        child = SerializationHelper.find_child_element(element, "FONT")
        if child is not None:
            font_value = EEnumFont.deserialize(child)
            obj.font = font_value

        # Parse sub
        child = SerializationHelper.find_child_element(element, "SUB")
        if child is not None:
            sub_value = child.text
            obj.sub = sub_value

        # Parse sup
        child = SerializationHelper.find_child_element(element, "SUP")
        if child is not None:
            sup_value = child.text
            obj.sup = sup_value

        # Parse tt
        child = SerializationHelper.find_child_element(element, "TT")
        if child is not None:
            tt_value = SerializationHelper.deserialize_by_tag(child, "Tt")
            obj.tt = tt_value

        # Parse type
        child = SerializationHelper.find_child_element(element, "TYPE")
        if child is not None:
            type_value = EEnum.deserialize(child)
            obj.type = type_value

        return obj



class EmphasisTextBuilder(BuilderBase):
    """Builder for EmphasisText with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EmphasisText = EmphasisText()


    def with_color(self, value: Optional[String]) -> "EmphasisTextBuilder":
        """Set color attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.color = value
        return self

    def with_font(self, value: Optional[EEnumFont]) -> "EmphasisTextBuilder":
        """Set font attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.font = value
        return self

    def with_sub(self, value: Superscript) -> "EmphasisTextBuilder":
        """Set sub attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sub = value
        return self

    def with_sup(self, value: Superscript) -> "EmphasisTextBuilder":
        """Set sup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sup = value
        return self

    def with_tt(self, value: Optional[Tt]) -> "EmphasisTextBuilder":
        """Set tt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tt = value
        return self

    def with_type(self, value: Optional[EEnum]) -> "EmphasisTextBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> EmphasisText:
        """Build and return the EmphasisText instance with validation."""
        self._validate_instance()
        pass
        return self._obj