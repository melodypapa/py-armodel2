"""TcpOptionFilterSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TcpOptionFilterSet(ARElement):
    """AUTOSAR TcpOptionFilterSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_option_filter_list_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TcpOptionFilterSet."""
        super().__init__()
        self.tcp_option_filter_list_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize TcpOptionFilterSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpOptionFilterSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_option_filter_list_refs (list to container "TCP-OPTION-FILTER-LIST-REFS")
        if self.tcp_option_filter_list_refs:
            wrapper = ET.Element("TCP-OPTION-FILTER-LIST-REFS")
            for item in self.tcp_option_filter_list_refs:
                serialized = SerializationHelper.serialize_item(item, "TcpOptionFilterList")
                if serialized is not None:
                    child_elem = ET.Element("TCP-OPTION-FILTER-LIST-REF")
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
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterSet":
        """Deserialize XML element to TcpOptionFilterSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpOptionFilterSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpOptionFilterSet, cls).deserialize(element)

        # Parse tcp_option_filter_list_refs (list from container "TCP-OPTION-FILTER-LIST-REFS")
        obj.tcp_option_filter_list_refs = []
        container = SerializationHelper.find_child_element(element, "TCP-OPTION-FILTER-LIST-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tcp_option_filter_list_refs.append(child_value)

        return obj



class TcpOptionFilterSetBuilder(ARElementBuilder):
    """Builder for TcpOptionFilterSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpOptionFilterSet = TcpOptionFilterSet()


    def with_tcp_option_filter_lists(self, items: list[TcpOptionFilterList]) -> "TcpOptionFilterSetBuilder":
        """Set tcp_option_filter_lists list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tcp_option_filter_lists = list(items) if items else []
        return self


    def add_tcp_option_filter_list(self, item: TcpOptionFilterList) -> "TcpOptionFilterSetBuilder":
        """Add a single item to tcp_option_filter_lists list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tcp_option_filter_lists.append(item)
        return self

    def clear_tcp_option_filter_lists(self) -> "TcpOptionFilterSetBuilder":
        """Clear all items from tcp_option_filter_lists list.

        Returns:
            self for method chaining
        """
        self._obj.tcp_option_filter_lists = []
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


    def build(self) -> TcpOptionFilterSet:
        """Build and return the TcpOptionFilterSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj