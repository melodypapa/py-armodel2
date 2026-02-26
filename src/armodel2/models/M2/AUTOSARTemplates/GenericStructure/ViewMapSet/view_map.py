"""ViewMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ViewMap(Identifiable):
    """AUTOSAR ViewMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_elements: list[AtpFeature]
    role: Optional[Identifier]
    second_elements: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize ViewMap."""
        super().__init__()
        self.first_elements: list[AtpFeature] = []
        self.role: Optional[Identifier] = None
        self.second_elements: list[AtpFeature] = []

    def serialize(self) -> ET.Element:
        """Serialize ViewMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ViewMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_elements (list to container "FIRST-ELEMENTS")
        if self.first_elements:
            wrapper = ET.Element("FIRST-ELEMENTS")
            for item in self.first_elements:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_elements (list to container "SECOND-ELEMENTS")
        if self.second_elements:
            wrapper = ET.Element("SECOND-ELEMENTS")
            for item in self.second_elements:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMap":
        """Deserialize XML element to ViewMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ViewMap, cls).deserialize(element)

        # Parse first_elements (list from container "FIRST-ELEMENTS")
        obj.first_elements = []
        container = SerializationHelper.find_child_element(element, "FIRST-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.first_elements.append(child_value)

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse second_elements (list from container "SECOND-ELEMENTS")
        obj.second_elements = []
        container = SerializationHelper.find_child_element(element, "SECOND-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.second_elements.append(child_value)

        return obj



class ViewMapBuilder(IdentifiableBuilder):
    """Builder for ViewMap with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ViewMap = ViewMap()


    def with_first_elements(self, items: list[AtpFeature]) -> "ViewMapBuilder":
        """Set first_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.first_elements = list(items) if items else []
        return self

    def with_role(self, value: Optional[Identifier]) -> "ViewMapBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_second_elements(self, items: list[AtpFeature]) -> "ViewMapBuilder":
        """Set second_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.second_elements = list(items) if items else []
        return self


    def add_first_element(self, item: AtpFeature) -> "ViewMapBuilder":
        """Add a single item to first_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.first_elements.append(item)
        return self

    def clear_first_elements(self) -> "ViewMapBuilder":
        """Clear all items from first_elements list.

        Returns:
            self for method chaining
        """
        self._obj.first_elements = []
        return self

    def add_second_element(self, item: AtpFeature) -> "ViewMapBuilder":
        """Add a single item to second_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.second_elements.append(item)
        return self

    def clear_second_elements(self) -> "ViewMapBuilder":
        """Clear all items from second_elements list.

        Returns:
            self for method chaining
        """
        self._obj.second_elements = []
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


    def build(self) -> ViewMap:
        """Build and return the ViewMap instance with validation."""
        self._validate_instance()
        pass
        return self._obj