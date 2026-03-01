"""MlFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 309)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Formula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MlFormula(Paginateable):
    """AUTOSAR MlFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ML-FORMULA"


    formula_caption: Optional[Caption]
    generic_math: Optional[MultiLanguagePlainText]
    l_graphics: list[LGraphic]
    tex_math: Optional[MultiLanguagePlainText]
    verbatim: Optional[MultiLanguageVerbatim]
    _DESERIALIZE_DISPATCH = {
        "FORMULA-CAPTION": lambda obj, elem: setattr(obj, "formula_caption", SerializationHelper.deserialize_by_tag(elem, "Caption")),
        "GENERIC-MATH": lambda obj, elem: setattr(obj, "generic_math", SerializationHelper.deserialize_by_tag(elem, "MultiLanguagePlainText")),
        "L-GRAPHICS": lambda obj, elem: obj.l_graphics.append(SerializationHelper.deserialize_by_tag(elem, "LGraphic")),
        "TEX-MATH": lambda obj, elem: setattr(obj, "tex_math", SerializationHelper.deserialize_by_tag(elem, "MultiLanguagePlainText")),
        "VERBATIM": lambda obj, elem: setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageVerbatim")),
    }


    def __init__(self) -> None:
        """Initialize MlFormula."""
        super().__init__()
        self.formula_caption: Optional[Caption] = None
        self.generic_math: Optional[MultiLanguagePlainText] = None
        self.l_graphics: list[LGraphic] = []
        self.tex_math: Optional[MultiLanguagePlainText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def serialize(self) -> ET.Element:
        """Serialize MlFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MlFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize formula_caption
        if self.formula_caption is not None:
            serialized = SerializationHelper.serialize_item(self.formula_caption, "Caption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize generic_math
        if self.generic_math is not None:
            serialized = SerializationHelper.serialize_item(self.generic_math, "MultiLanguagePlainText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GENERIC-MATH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l_graphics (list to container "L-GRAPHICS")
        if self.l_graphics:
            wrapper = ET.Element("L-GRAPHICS")
            for item in self.l_graphics:
                serialized = SerializationHelper.serialize_item(item, "LGraphic")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tex_math
        if self.tex_math is not None:
            serialized = SerializationHelper.serialize_item(self.tex_math, "MultiLanguagePlainText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEX-MATH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim
        if self.verbatim is not None:
            serialized = SerializationHelper.serialize_item(self.verbatim, "MultiLanguageVerbatim")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERBATIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MlFormula":
        """Deserialize XML element to MlFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MlFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MlFormula, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "FORMULA-CAPTION":
                setattr(obj, "formula_caption", SerializationHelper.deserialize_by_tag(child, "Caption"))
            elif tag == "GENERIC-MATH":
                setattr(obj, "generic_math", SerializationHelper.deserialize_by_tag(child, "MultiLanguagePlainText"))
            elif tag == "L-GRAPHICS":
                obj.l_graphics.append(SerializationHelper.deserialize_by_tag(child, "LGraphic"))
            elif tag == "TEX-MATH":
                setattr(obj, "tex_math", SerializationHelper.deserialize_by_tag(child, "MultiLanguagePlainText"))
            elif tag == "VERBATIM":
                setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(child, "MultiLanguageVerbatim"))

        return obj



class MlFormulaBuilder(PaginateableBuilder):
    """Builder for MlFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MlFormula = MlFormula()


    def with_formula_caption(self, value: Optional[Caption]) -> "MlFormulaBuilder":
        """Set formula_caption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.formula_caption = value
        return self

    def with_generic_math(self, value: Optional[MultiLanguagePlainText]) -> "MlFormulaBuilder":
        """Set generic_math attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.generic_math = value
        return self

    def with_l_graphics(self, items: list[LGraphic]) -> "MlFormulaBuilder":
        """Set l_graphics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.l_graphics = list(items) if items else []
        return self

    def with_tex_math(self, value: Optional[MultiLanguagePlainText]) -> "MlFormulaBuilder":
        """Set tex_math attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tex_math = value
        return self

    def with_verbatim(self, value: Optional[MultiLanguageVerbatim]) -> "MlFormulaBuilder":
        """Set verbatim attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.verbatim = value
        return self


    def add_l_graphic(self, item: LGraphic) -> "MlFormulaBuilder":
        """Add a single item to l_graphics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.l_graphics.append(item)
        return self

    def clear_l_graphics(self) -> "MlFormulaBuilder":
        """Clear all items from l_graphics list.

        Returns:
            self for method chaining
        """
        self._obj.l_graphics = []
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


    def build(self) -> MlFormula:
        """Build and return the MlFormula instance with validation."""
        self._validate_instance()
        pass
        return self._obj