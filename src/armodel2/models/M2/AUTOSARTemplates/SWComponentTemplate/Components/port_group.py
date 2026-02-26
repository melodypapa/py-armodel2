"""PortGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortGroup(Identifiable):
    """AUTOSAR PortGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_group_refs: list[ARRef]
    outer_port_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PortGroup."""
        super().__init__()
        self.inner_group_refs: list[ARRef] = []
        self.outer_port_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PortGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_group_refs (list to container "INNER-GROUP-REFS")
        if self.inner_group_refs:
            wrapper = ET.Element("INNER-GROUP-REFS")
            for item in self.inner_group_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("INNER-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize outer_port_refs (list to container "OUTER-PORT-REFS")
        if self.outer_port_refs:
            wrapper = ET.Element("OUTER-PORT-REFS")
            for item in self.outer_port_refs:
                serialized = SerializationHelper.serialize_item(item, "PortPrototype")
                if serialized is not None:
                    child_elem = ET.Element("OUTER-PORT-REF")
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
    def deserialize(cls, element: ET.Element) -> "PortGroup":
        """Deserialize XML element to PortGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortGroup, cls).deserialize(element)

        # Parse inner_group_refs (list from container "INNER-GROUP-REFS")
        obj.inner_group_refs = []
        container = SerializationHelper.find_child_element(element, "INNER-GROUP-REFS")
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
                    obj.inner_group_refs.append(child_value)

        # Parse outer_port_refs (list from container "OUTER-PORT-REFS")
        obj.outer_port_refs = []
        container = SerializationHelper.find_child_element(element, "OUTER-PORT-REFS")
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
                    obj.outer_port_refs.append(child_value)

        return obj



class PortGroupBuilder(IdentifiableBuilder):
    """Builder for PortGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortGroup = PortGroup()


    def with_inner_groups(self, items: list[PortGroup]) -> "PortGroupBuilder":
        """Set inner_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.inner_groups = list(items) if items else []
        return self

    def with_outer_ports(self, items: list[PortPrototype]) -> "PortGroupBuilder":
        """Set outer_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.outer_ports = list(items) if items else []
        return self


    def add_inner_group(self, item: PortGroup) -> "PortGroupBuilder":
        """Add a single item to inner_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.inner_groups.append(item)
        return self

    def clear_inner_groups(self) -> "PortGroupBuilder":
        """Clear all items from inner_groups list.

        Returns:
            self for method chaining
        """
        self._obj.inner_groups = []
        return self

    def add_outer_port(self, item: PortPrototype) -> "PortGroupBuilder":
        """Add a single item to outer_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.outer_ports.append(item)
        return self

    def clear_outer_ports(self) -> "PortGroupBuilder":
        """Clear all items from outer_ports list.

        Returns:
            self for method chaining
        """
        self._obj.outer_ports = []
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


    def build(self) -> PortGroup:
        """Build and return the PortGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj