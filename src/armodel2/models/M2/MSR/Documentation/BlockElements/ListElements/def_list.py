"""DefList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.def_item import (
        DefItem,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DefList(Paginateable):
    """AUTOSAR DefList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DEF-LIST"


    def_item: DefItem
    _DESERIALIZE_DISPATCH = {
        "DEF-ITEM": lambda obj, elem: setattr(obj, "def_item", SerializationHelper.deserialize_by_tag(elem, "DefItem")),
    }


    def __init__(self) -> None:
        """Initialize DefList."""
        super().__init__()
        self.def_item: DefItem = None

    def serialize(self) -> ET.Element:
        """Serialize DefList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DefList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize def_item
        if self.def_item is not None:
            serialized = SerializationHelper.serialize_item(self.def_item, "DefItem")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF-ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefList":
        """Deserialize XML element to DefList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DefList, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEF-ITEM":
                setattr(obj, "def_item", SerializationHelper.deserialize_by_tag(child, "DefItem"))

        return obj



class DefListBuilder(PaginateableBuilder):
    """Builder for DefList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DefList = DefList()


    def with_def_item(self, value: DefItem) -> "DefListBuilder":
        """Set def_item attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'def_item' is required and cannot be None")
        self._obj.def_item = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "defItem",
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
        if getattr(self._obj, "defItem", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'defItem' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'defItem' is None", UserWarning)


    def build(self) -> DefList:
        """Build and return the DefList instance with validation."""
        self._validate_instance()
        return self._obj