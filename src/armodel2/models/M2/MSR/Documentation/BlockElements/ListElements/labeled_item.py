"""LabeledItem AUTOSAR element.

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
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class LabeledItem(Paginateable):
    """AUTOSAR LabeledItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LABELED-ITEM"


    help_entry: Optional[String]
    item_contents: Optional[DocumentationBlock]
    item_label: MultiLanguageOverviewParagraph
    _DESERIALIZE_DISPATCH = {
        "HELP-ENTRY": lambda obj, elem: setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ITEM-CONTENTS": lambda obj, elem: setattr(obj, "item_contents", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "ITEM-LABEL": lambda obj, elem: setattr(obj, "item_label", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageOverviewParagraph")),
    }


    def __init__(self) -> None:
        """Initialize LabeledItem."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.item_contents: Optional[DocumentationBlock] = None
        self.item_label: MultiLanguageOverviewParagraph = None

    def serialize(self) -> ET.Element:
        """Serialize LabeledItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LabeledItem, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = SerializationHelper.serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize item_contents
        if self.item_contents is not None:
            serialized = SerializationHelper.serialize_item(self.item_contents, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize item_label
        if self.item_label is not None:
            serialized = SerializationHelper.serialize_item(self.item_label, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledItem":
        """Deserialize XML element to LabeledItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LabeledItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LabeledItem, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HELP-ENTRY":
                setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ITEM-CONTENTS":
                setattr(obj, "item_contents", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "ITEM-LABEL":
                setattr(obj, "item_label", SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph"))

        return obj



class LabeledItemBuilder(PaginateableBuilder):
    """Builder for LabeledItem with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LabeledItem = LabeledItem()


    def with_help_entry(self, value: Optional[String]) -> "LabeledItemBuilder":
        """Set help_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'help_entry' is required and cannot be None")
        self._obj.help_entry = value
        return self

    def with_item_contents(self, value: Optional[DocumentationBlock]) -> "LabeledItemBuilder":
        """Set item_contents attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'item_contents' is required and cannot be None")
        self._obj.item_contents = value
        return self

    def with_item_label(self, value: MultiLanguageOverviewParagraph) -> "LabeledItemBuilder":
        """Set item_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'item_label' is required and cannot be None")
        self._obj.item_label = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "itemLabel",
    }
    _OPTIONAL_ATTRIBUTES = {
        "helpEntry",
        "itemContents",
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
        if getattr(self._obj, "itemLabel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'itemLabel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'itemLabel' is None", UserWarning)


    def build(self) -> LabeledItem:
        """Build and return the LabeledItem instance with validation."""
        self._validate_instance()
        return self._obj