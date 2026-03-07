"""LabeledList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.indent_sample import (
    IndentSample,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_item import (
        LabeledItem,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class LabeledList(Paginateable):
    """AUTOSAR LabeledList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LABELED-LIST"


    indent_sample: Optional[IndentSample]
    labeled_item_label: LabeledItem
    _DESERIALIZE_DISPATCH = {
        "INDENT-SAMPLE": lambda obj, elem: setattr(obj, "indent_sample", SerializationHelper.deserialize_by_tag(elem, "IndentSample")),
        "LABELED-ITEM-LABEL": lambda obj, elem: setattr(obj, "labeled_item_label", SerializationHelper.deserialize_by_tag(elem, "LabeledItem")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INDENT-SAMPLE":
                setattr(obj, "indent_sample", SerializationHelper.deserialize_by_tag(child, "IndentSample"))
            elif tag == "LABELED-ITEM-LABEL":
                setattr(obj, "labeled_item_label", SerializationHelper.deserialize_by_tag(child, "LabeledItem"))

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
            raise ValueError("Attribute 'indent_sample' is required and cannot be None")
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
            raise ValueError("Attribute 'labeled_item_label' is required and cannot be None")
        self._obj.labeled_item_label = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "labeledItemLabel",
    }
    _OPTIONAL_ATTRIBUTES = {
        "indentSample",
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
        if getattr(self._obj, "labeledItemLabel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'labeledItemLabel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'labeledItemLabel' is None", UserWarning)


    def build(self) -> LabeledList:
        """Build and return the LabeledList instance with validation."""
        self._validate_instance()
        return self._obj