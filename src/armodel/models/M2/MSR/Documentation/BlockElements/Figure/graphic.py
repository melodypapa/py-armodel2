"""Graphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 302)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_attribute

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    GraphicFitEnum,
    GraphicNotationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Graphic(EngineeringObject):
    """AUTOSAR Graphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse editfit
        child = SerializationHelper.find_child_element(element, "EDITFIT")
        if child is not None:
            editfit_value = GraphicFitEnum.deserialize(child)
            obj.editfit = editfit_value

        # Parse edit_height
        child = SerializationHelper.find_child_element(element, "EDIT-HEIGHT")
        if child is not None:
            edit_height_value = child.text
            obj.edit_height = edit_height_value

        # Parse editscale
        child = SerializationHelper.find_child_element(element, "EDITSCALE")
        if child is not None:
            editscale_value = child.text
            obj.editscale = editscale_value

        # Parse edit_width
        child = SerializationHelper.find_child_element(element, "EDIT-WIDTH")
        if child is not None:
            edit_width_value = child.text
            obj.edit_width = edit_width_value

        # Parse filename from XML attribute
        if "FILENAME" in element.attrib:
            filename_value = element.attrib["FILENAME"]
            obj.filename = filename_value

        # Parse fit
        child = SerializationHelper.find_child_element(element, "FIT")
        if child is not None:
            fit_value = GraphicFitEnum.deserialize(child)
            obj.fit = fit_value

        # Parse generator
        child = SerializationHelper.find_child_element(element, "GENERATOR")
        if child is not None:
            generator_value = child.text
            obj.generator = generator_value

        # Parse height
        child = SerializationHelper.find_child_element(element, "HEIGHT")
        if child is not None:
            height_value = child.text
            obj.height = height_value

        # Parse html_fit
        child = SerializationHelper.find_child_element(element, "HTML-FIT")
        if child is not None:
            html_fit_value = GraphicFitEnum.deserialize(child)
            obj.html_fit = html_fit_value

        # Parse html_height
        child = SerializationHelper.find_child_element(element, "HTML-HEIGHT")
        if child is not None:
            html_height_value = child.text
            obj.html_height = html_height_value

        # Parse html_scale
        child = SerializationHelper.find_child_element(element, "HTML-SCALE")
        if child is not None:
            html_scale_value = child.text
            obj.html_scale = html_scale_value

        # Parse html_width
        child = SerializationHelper.find_child_element(element, "HTML-WIDTH")
        if child is not None:
            html_width_value = child.text
            obj.html_width = html_width_value

        # Parse notation
        child = SerializationHelper.find_child_element(element, "NOTATION")
        if child is not None:
            notation_value = GraphicNotationEnum.deserialize(child)
            obj.notation = notation_value

        # Parse scale
        child = SerializationHelper.find_child_element(element, "SCALE")
        if child is not None:
            scale_value = child.text
            obj.scale = scale_value

        # Parse width
        child = SerializationHelper.find_child_element(element, "WIDTH")
        if child is not None:
            width_value = child.text
            obj.width = width_value

        return obj



class GraphicBuilder:
    """Builder for Graphic with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: Graphic = Graphic()


    def with_category(self, value: NameToken) -> "GraphicBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_domain(self, value: Optional[NameToken]) -> "GraphicBuilder":
        """Set domain attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.domain = value
        return self

    def with_revision_labels(self, items: list[RevisionLabelString]) -> "GraphicBuilder":
        """Set revision_labels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.revision_labels = list(items) if items else []
        return self

    def with_short_label(self, value: NameToken) -> "GraphicBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

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


    def add_revision_label(self, item: RevisionLabelString) -> "GraphicBuilder":
        """Add a single item to revision_labels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.revision_labels.append(item)
        return self

    def clear_revision_labels(self) -> "GraphicBuilder":
        """Clear all items from revision_labels list.

        Returns:
            self for method chaining
        """
        self._obj.revision_labels = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> Graphic:
        """Build and return the Graphic instance with validation."""
        self._validate_instance()
        pass
        return self._obj