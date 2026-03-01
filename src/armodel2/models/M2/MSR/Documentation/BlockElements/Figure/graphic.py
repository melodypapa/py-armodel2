"""Graphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 302)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_attribute

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import EngineeringObjectBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.Figure import (
    GraphicFitEnum,
    GraphicNotationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Graphic(EngineeringObject):
    """AUTOSAR Graphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GRAPHIC"


    editfit: Optional[GraphicFitEnum]
    edit_height: Optional[String]
    editscale: Optional[String]
    edit_width: Optional[String]
    _filename: Optional[String]
    fit: Optional[GraphicFitEnum]
    generator: Optional[NameToken]
    height: Optional[String]
    html_fit: Optional[GraphicFitEnum]
    html_height: Optional[String]
    html_scale: Optional[String]
    html_width: Optional[String]
    notation: Optional[GraphicNotationEnum]
    scale: Optional[String]
    width: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "EDITFIT": lambda obj, elem: setattr(obj, "editfit", GraphicFitEnum.deserialize(elem)),
        "EDIT-HEIGHT": lambda obj, elem: setattr(obj, "edit_height", SerializationHelper.deserialize_by_tag(elem, "String")),
        "EDITSCALE": lambda obj, elem: setattr(obj, "editscale", SerializationHelper.deserialize_by_tag(elem, "String")),
        "EDIT-WIDTH": lambda obj, elem: setattr(obj, "edit_width", SerializationHelper.deserialize_by_tag(elem, "String")),
        "FIT": lambda obj, elem: setattr(obj, "fit", GraphicFitEnum.deserialize(elem)),
        "GENERATOR": lambda obj, elem: setattr(obj, "generator", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "HEIGHT": lambda obj, elem: setattr(obj, "height", SerializationHelper.deserialize_by_tag(elem, "String")),
        "HTML-FIT": lambda obj, elem: setattr(obj, "html_fit", GraphicFitEnum.deserialize(elem)),
        "HTML-HEIGHT": lambda obj, elem: setattr(obj, "html_height", SerializationHelper.deserialize_by_tag(elem, "String")),
        "HTML-SCALE": lambda obj, elem: setattr(obj, "html_scale", SerializationHelper.deserialize_by_tag(elem, "String")),
        "HTML-WIDTH": lambda obj, elem: setattr(obj, "html_width", SerializationHelper.deserialize_by_tag(elem, "String")),
        "NOTATION": lambda obj, elem: setattr(obj, "notation", GraphicNotationEnum.deserialize(elem)),
        "SCALE": lambda obj, elem: setattr(obj, "scale", SerializationHelper.deserialize_by_tag(elem, "String")),
        "WIDTH": lambda obj, elem: setattr(obj, "width", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize Graphic."""
        super().__init__()
        self.editfit: Optional[GraphicFitEnum] = None
        self.edit_height: Optional[String] = None
        self.editscale: Optional[String] = None
        self.edit_width: Optional[String] = None
        self._filename: Optional[String] = None
        self.fit: Optional[GraphicFitEnum] = None
        self.generator: Optional[NameToken] = None
        self.height: Optional[String] = None
        self.html_fit: Optional[GraphicFitEnum] = None
        self.html_height: Optional[String] = None
        self.html_scale: Optional[String] = None
        self.html_width: Optional[String] = None
        self.notation: Optional[GraphicNotationEnum] = None
        self.scale: Optional[String] = None
        self.width: Optional[String] = None
    @property
    @xml_attribute
    def filename(self) -> String:
        """Get filename XML attribute."""
        return self._filename

    @filename.setter
    def filename(self, value: String) -> None:
        """Set filename XML attribute."""
        self._filename = value


    def serialize(self) -> ET.Element:
        """Serialize Graphic to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Graphic, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize editfit
        if self.editfit is not None:
            serialized = SerializationHelper.serialize_item(self.editfit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDITFIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize edit_height
        if self.edit_height is not None:
            serialized = SerializationHelper.serialize_item(self.edit_height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDIT-HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize editscale
        if self.editscale is not None:
            serialized = SerializationHelper.serialize_item(self.editscale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDITSCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize edit_width
        if self.edit_width is not None:
            serialized = SerializationHelper.serialize_item(self.edit_width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EDIT-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filename as XML attribute
        if self.filename is not None:
            elem.attrib["FILENAME"] = str(self.filename)

        # Serialize fit
        if self.fit is not None:
            serialized = SerializationHelper.serialize_item(self.fit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize generator
        if self.generator is not None:
            serialized = SerializationHelper.serialize_item(self.generator, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GENERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize height
        if self.height is not None:
            serialized = SerializationHelper.serialize_item(self.height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_fit
        if self.html_fit is not None:
            serialized = SerializationHelper.serialize_item(self.html_fit, "GraphicFitEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-FIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_height
        if self.html_height is not None:
            serialized = SerializationHelper.serialize_item(self.html_height, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-HEIGHT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_scale
        if self.html_scale is not None:
            serialized = SerializationHelper.serialize_item(self.html_scale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-SCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize html_width
        if self.html_width is not None:
            serialized = SerializationHelper.serialize_item(self.html_width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HTML-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize notation
        if self.notation is not None:
            serialized = SerializationHelper.serialize_item(self.notation, "GraphicNotationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scale
        if self.scale is not None:
            serialized = SerializationHelper.serialize_item(self.scale, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize width
        if self.width is not None:
            serialized = SerializationHelper.serialize_item(self.width, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Graphic":
        """Deserialize XML element to Graphic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Graphic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Graphic, cls).deserialize(element)

        # Parse filename from XML attribute
        if "FILENAME" in element.attrib:
            obj.filename = element.attrib["FILENAME"]

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EDITFIT":
                setattr(obj, "editfit", GraphicFitEnum.deserialize(child))
            elif tag == "EDIT-HEIGHT":
                setattr(obj, "edit_height", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "EDITSCALE":
                setattr(obj, "editscale", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "EDIT-WIDTH":
                setattr(obj, "edit_width", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "FIT":
                setattr(obj, "fit", GraphicFitEnum.deserialize(child))
            elif tag == "GENERATOR":
                setattr(obj, "generator", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "HEIGHT":
                setattr(obj, "height", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "HTML-FIT":
                setattr(obj, "html_fit", GraphicFitEnum.deserialize(child))
            elif tag == "HTML-HEIGHT":
                setattr(obj, "html_height", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "HTML-SCALE":
                setattr(obj, "html_scale", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "HTML-WIDTH":
                setattr(obj, "html_width", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "NOTATION":
                setattr(obj, "notation", GraphicNotationEnum.deserialize(child))
            elif tag == "SCALE":
                setattr(obj, "scale", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "WIDTH":
                setattr(obj, "width", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class GraphicBuilder(EngineeringObjectBuilder):
    """Builder for Graphic with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Graphic = Graphic()


    def with_editfit(self, value: Optional[GraphicFitEnum]) -> "GraphicBuilder":
        """Set editfit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.editfit = value
        return self

    def with_edit_height(self, value: Optional[String]) -> "GraphicBuilder":
        """Set edit_height attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.edit_height = value
        return self

    def with_editscale(self, value: Optional[String]) -> "GraphicBuilder":
        """Set editscale attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.editscale = value
        return self

    def with_edit_width(self, value: Optional[String]) -> "GraphicBuilder":
        """Set edit_width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.edit_width = value
        return self

    def with_filename(self, value: Optional[String]) -> "GraphicBuilder":
        """Set filename attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filename = value
        return self

    def with_fit(self, value: Optional[GraphicFitEnum]) -> "GraphicBuilder":
        """Set fit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fit = value
        return self

    def with_generator(self, value: Optional[NameToken]) -> "GraphicBuilder":
        """Set generator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.generator = value
        return self

    def with_height(self, value: Optional[String]) -> "GraphicBuilder":
        """Set height attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.height = value
        return self

    def with_html_fit(self, value: Optional[GraphicFitEnum]) -> "GraphicBuilder":
        """Set html_fit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.html_fit = value
        return self

    def with_html_height(self, value: Optional[String]) -> "GraphicBuilder":
        """Set html_height attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.html_height = value
        return self

    def with_html_scale(self, value: Optional[String]) -> "GraphicBuilder":
        """Set html_scale attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.html_scale = value
        return self

    def with_html_width(self, value: Optional[String]) -> "GraphicBuilder":
        """Set html_width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.html_width = value
        return self

    def with_notation(self, value: Optional[GraphicNotationEnum]) -> "GraphicBuilder":
        """Set notation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.notation = value
        return self

    def with_scale(self, value: Optional[String]) -> "GraphicBuilder":
        """Set scale attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scale = value
        return self

    def with_width(self, value: Optional[String]) -> "GraphicBuilder":
        """Set width attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.width = value
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


    def build(self) -> Graphic:
        """Build and return the Graphic instance with validation."""
        self._validate_instance()
        pass
        return self._obj