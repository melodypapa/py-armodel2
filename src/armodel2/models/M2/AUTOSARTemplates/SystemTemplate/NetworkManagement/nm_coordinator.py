"""NmCoordinator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
        NmNode,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NmCoordinator(ARObject):
    """AUTOSAR NmCoordinator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NM-COORDINATOR"


    index: Optional[Integer]
    nm_coord_sync: Optional[Boolean]
    nm_global: Optional[TimeValue]
    nm_node_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INDEX": lambda obj, elem: setattr(obj, "index", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NM-COORD-SYNC": lambda obj, elem: setattr(obj, "nm_coord_sync", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-GLOBAL": lambda obj, elem: setattr(obj, "nm_global", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-NODES": ("_POLYMORPHIC_LIST", "nm_node_refs", ["CanNmNode", "FlexrayNmNode", "J1939NmNode", "UdpNmNode"]),
    }


    def __init__(self) -> None:
        """Initialize NmCoordinator."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.nm_coord_sync: Optional[Boolean] = None
        self.nm_global: Optional[TimeValue] = None
        self.nm_node_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize NmCoordinator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmCoordinator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize index
        if self.index is not None:
            serialized = SerializationHelper.serialize_item(self.index, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coord_sync
        if self.nm_coord_sync is not None:
            serialized = SerializationHelper.serialize_item(self.nm_coord_sync, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORD-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_global
        if self.nm_global is not None:
            serialized = SerializationHelper.serialize_item(self.nm_global, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-GLOBAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node_refs (list to container "NM-NODE-REFS")
        if self.nm_node_refs:
            wrapper = ET.Element("NM-NODE-REFS")
            for item in self.nm_node_refs:
                serialized = SerializationHelper.serialize_item(item, "NmNode")
                if serialized is not None:
                    child_elem = ET.Element("NM-NODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCoordinator":
        """Deserialize XML element to NmCoordinator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmCoordinator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmCoordinator, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INDEX":
                setattr(obj, "index", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "NM-COORD-SYNC":
                setattr(obj, "nm_coord_sync", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-GLOBAL":
                setattr(obj, "nm_global", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-NODES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-NM-NODE":
                        obj.nm_node_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanNmNode"))
                    elif concrete_tag == "FLEXRAY-NM-NODE":
                        obj.nm_node_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayNmNode"))
                    elif concrete_tag == "J1939-NM-NODE":
                        obj.nm_node_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939NmNode"))
                    elif concrete_tag == "UDP-NM-NODE":
                        obj.nm_node_refs.append(SerializationHelper.deserialize_by_tag(child[0], "UdpNmNode"))

        return obj



class NmCoordinatorBuilder(BuilderBase):
    """Builder for NmCoordinator with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmCoordinator = NmCoordinator()


    def with_index(self, value: Optional[Integer]) -> "NmCoordinatorBuilder":
        """Set index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.index = value
        return self

    def with_nm_coord_sync(self, value: Optional[Boolean]) -> "NmCoordinatorBuilder":
        """Set nm_coord_sync attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_coord_sync = value
        return self

    def with_nm_global(self, value: Optional[TimeValue]) -> "NmCoordinatorBuilder":
        """Set nm_global attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_global = value
        return self

    def with_nm_nodes(self, items: list[NmNode]) -> "NmCoordinatorBuilder":
        """Set nm_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_nodes = list(items) if items else []
        return self


    def add_nm_node(self, item: NmNode) -> "NmCoordinatorBuilder":
        """Add a single item to nm_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_nodes.append(item)
        return self

    def clear_nm_nodes(self) -> "NmCoordinatorBuilder":
        """Clear all items from nm_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.nm_nodes = []
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


    def build(self) -> NmCoordinator:
        """Build and return the NmCoordinator instance with validation."""
        self._validate_instance()
        pass
        return self._obj