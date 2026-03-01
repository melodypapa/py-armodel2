"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "REFERENCE-BASE"


    short_label: Identifier
    is_default: Boolean
    is_global: Boolean
    base_is_this_package: Boolean
    package_ref: Optional[ARRef]
    global_element_refs: list[ReferrableSubtypesEnum]
    global_in_package_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "IS-DEFAULT": lambda obj, elem: setattr(obj, "is_default", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IS-GLOBAL": lambda obj, elem: setattr(obj, "is_global", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "BASE-IS-THIS-PACKAGE": lambda obj, elem: setattr(obj, "base_is_this_package", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PACKAGE-REF": lambda obj, elem: setattr(obj, "package_ref", ARRef.deserialize(elem)),
        "GLOBAL-ELEMENTS": lambda obj, elem: obj.global_element_refs.append(ARRef.deserialize(elem)),
        "GLOBAL-IN-PACKAGES": lambda obj, elem: obj.global_in_package_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.short_label: Identifier = None
        self.is_default: Boolean = None
        self.is_global: Boolean = None
        self.base_is_this_package: Boolean = None
        self.package_ref: Optional[ARRef] = None
        self.global_element_refs: list[ReferrableSubtypesEnum] = []
        self.global_in_package_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ReferenceBase to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReferenceBase, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_default
        if self.is_default is not None:
            serialized = SerializationHelper.serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_global
        if self.is_global is not None:
            serialized = SerializationHelper.serialize_item(self.is_global, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-GLOBAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_is_this_package
        if self.base_is_this_package is not None:
            serialized = SerializationHelper.serialize_item(self.base_is_this_package, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-IS-THIS-PACKAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize package_ref
        if self.package_ref is not None:
            serialized = SerializationHelper.serialize_item(self.package_ref, "ARPackage")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_element_refs (list to container "GLOBAL-ELEMENT-REFS")
        if self.global_element_refs:
            wrapper = ET.Element("GLOBAL-ELEMENT-REFS")
            for item in self.global_element_refs:
                serialized = SerializationHelper.serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_in_package_refs (list to container "GLOBAL-IN-PACKAGE-REFS")
        if self.global_in_package_refs:
            wrapper = ET.Element("GLOBAL-IN-PACKAGE-REFS")
            for item in self.global_in_package_refs:
                serialized = SerializationHelper.serialize_item(item, "ARPackage")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-IN-PACKAGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Deserialize XML element to ReferenceBase object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceBase object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceBase, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "IS-DEFAULT":
                setattr(obj, "is_default", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IS-GLOBAL":
                setattr(obj, "is_global", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "BASE-IS-THIS-PACKAGE":
                setattr(obj, "base_is_this_package", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PACKAGE-REF":
                setattr(obj, "package_ref", ARRef.deserialize(child))
            elif tag == "GLOBAL-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.global_element_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ReferrableSubtypesEnum"))
            elif tag == "GLOBAL-IN-PACKAGES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.global_in_package_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ARPackage"))

        return obj



class ReferenceBaseBuilder(BuilderBase):
    """Builder for ReferenceBase with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ReferenceBase = ReferenceBase()


    def with_short_label(self, value: Identifier) -> "ReferenceBaseBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_is_default(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set is_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_default = value
        return self

    def with_is_global(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set is_global attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_global = value
        return self

    def with_base_is_this_package(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set base_is_this_package attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_is_this_package = value
        return self

    def with_package(self, value: Optional[ARPackage]) -> "ReferenceBaseBuilder":
        """Set package attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.package = value
        return self

    def with_global_elements(self, items: list[ReferrableSubtypesEnum]) -> "ReferenceBaseBuilder":
        """Set global_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.global_elements = list(items) if items else []
        return self

    def with_global_in_packages(self, items: list[ARPackage]) -> "ReferenceBaseBuilder":
        """Set global_in_packages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages = list(items) if items else []
        return self


    def add_global_element(self, item: ReferrableSubtypesEnum) -> "ReferenceBaseBuilder":
        """Add a single item to global_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.global_elements.append(item)
        return self

    def clear_global_elements(self) -> "ReferenceBaseBuilder":
        """Clear all items from global_elements list.

        Returns:
            self for method chaining
        """
        self._obj.global_elements = []
        return self

    def add_global_in_package(self, item: ARPackage) -> "ReferenceBaseBuilder":
        """Add a single item to global_in_packages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages.append(item)
        return self

    def clear_global_in_packages(self) -> "ReferenceBaseBuilder":
        """Clear all items from global_in_packages list.

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages = []
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


    def build(self) -> ReferenceBase:
        """Build and return the ReferenceBase instance with validation."""
        self._validate_instance()
        pass
        return self._obj