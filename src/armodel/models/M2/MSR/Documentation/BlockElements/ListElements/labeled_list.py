"""LabeledList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.indent_sample import (
    IndentSample,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_item import (
        LabeledItem,
    )



class LabeledList(Paginateable):
    """AUTOSAR LabeledList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    indent_sample: Optional[IndentSample]
    labeled_item_label: LabeledItem
    def __init__(self) -> None:
        """Initialize LabeledList."""
        super().__init__()
        self.indent_sample: Optional[IndentSample] = None
        self.labeled_item_label: LabeledItem = None

    def serialize(self) -> ET.Element:
        """Serialize LabeledList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LabeledList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize indent_sample
        if self.indent_sample is not None:
            serialized = SerializationHelper.serialize_item(self.indent_sample, "IndentSample")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDENT-SAMPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize labeled_item_label
        if self.labeled_item_label is not None:
            serialized = SerializationHelper.serialize_item(self.labeled_item_label, "LabeledItem")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABELED-ITEM-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledList":
        """Deserialize XML element to LabeledList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LabeledList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LabeledList, cls).deserialize(element)

        # Parse indent_sample
        child = SerializationHelper.find_child_element(element, "INDENT-SAMPLE")
        if child is not None:
            indent_sample_value = SerializationHelper.deserialize_by_tag(child, "IndentSample")
            obj.indent_sample = indent_sample_value

        # Parse labeled_item_label
        child = SerializationHelper.find_child_element(element, "LABELED-ITEM-LABEL")
        if child is not None:
            labeled_item_label_value = SerializationHelper.deserialize_by_tag(child, "LabeledItem")
            obj.labeled_item_label = labeled_item_label_value

        return obj



class LabeledListBuilder(PaginateableBuilder):
    """Builder for LabeledList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LabeledList = LabeledList()


    def with_indent_sample(self, value: Optional[IndentSample]) -> "LabeledListBuilder":
        """Set indent_sample attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.indent_sample = value
        return self

    def with_labeled_item_label(self, value: LabeledItem) -> "LabeledListBuilder":
        """Set labeled_item_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.labeled_item_label = value
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


    def build(self) -> LabeledList:
        """Build and return the LabeledList instance with validation."""
        self._validate_instance()
        pass
        return self._obj