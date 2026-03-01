"""ARList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_attribute
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ListEnum,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
        Item,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ARList(Paginateable):
    """AUTOSAR ARList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "AR-LIST"


    _items: list[Item]
    _type: Optional[ListEnum]
    _DESERIALIZE_DISPATCH = {
        "ITEMS": lambda obj, elem: obj._items.append(SerializationHelper.deserialize_by_tag(elem, "Item")),
    }


    def __init__(self) -> None:
        """Initialize ARList."""
        super().__init__()
        self._items: list[Item] = []
        self._type: Optional[ListEnum] = None
    @property
    @xml_element_name("ITEM")
    def items(self) -> list[Item]:
        """Get items with custom XML element name."""
        return self._items

    @items.setter
    def items(self, value: list[Item]) -> None:
        """Set items with custom XML element name."""
        self._items = value

    @property
    @xml_attribute
    def type(self) -> ListEnum:
        """Get type XML attribute."""
        return self._type

    @type.setter
    def type(self, value: ListEnum) -> None:
        """Set type XML attribute."""
        self._type = value


    def serialize(self) -> ET.Element:
        """Serialize ARList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ARList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize items (list of direct "ITEM" children, no container)
        if self.items:
            for item in self.items:
                serialized = SerializationHelper.serialize_item(item, "Item")
                if serialized is not None:
                    child_elem = ET.Element("ITEM")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    elem.append(child_elem)
        # Serialize type as XML attribute
        if self.type is not None:
            elem.attrib["TYPE"] = str(self.type)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARList":
        """Deserialize XML element to ARList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ARList, cls).deserialize(element)

        # Parse type from XML attribute
        if "TYPE" in element.attrib:
            obj.type = element.attrib["TYPE"]

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ITEMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._items.append(SerializationHelper.deserialize_by_tag(item_elem, "Item"))

        return obj



class ARListBuilder(BuilderBase):
    """Builder for ARList with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ARList = ARList()


    def with_items(self, items: list[Item]) -> "ARListBuilder":
        """Set items list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.items = list(items) if items else []
        return self

    def with_type(self, value: Optional[ListEnum]) -> "ARListBuilder":
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


    def add_item(self, item: Item) -> "ARListBuilder":
        """Add a single item to items list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.items.append(item)
        return self

    def clear_items(self) -> "ARListBuilder":
        """Clear all items from items list.

        Returns:
            self for method chaining
        """
        self._obj.items = []
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


    def build(self) -> ARList:
        """Build and return the ARList instance with validation."""
        self._validate_instance()
        pass
        return self._obj