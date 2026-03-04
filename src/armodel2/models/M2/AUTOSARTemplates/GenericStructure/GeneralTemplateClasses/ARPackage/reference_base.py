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
        "GLOBAL-ELEMENT-REFS": lambda obj, elem: [obj.global_element_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "GLOBAL-IN-PACKAGE-REFS": lambda obj, elem: [obj.global_in_package_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
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
            elif tag == "GLOBAL-ELEMENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.global_element_refs.append(ARRef.deserialize(item_elem))
            elif tag == "GLOBAL-IN-PACKAGE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.global_in_package_refs.append(ARRef.deserialize(item_elem))

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


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "baseIsThisPackage",
        "isDefault",
        "isGlobal",
        "shortLabel",
    }
    _OPTIONAL_ATTRIBUTES = {
        "globalElement",
        "globalInPackage",
        "package",
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
        if getattr(self._obj, "baseIsThisPackage", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'baseIsThisPackage' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'baseIsThisPackage' is None", UserWarning)
        if getattr(self._obj, "isDefault", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'isDefault' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'isDefault' is None", UserWarning)
        if getattr(self._obj, "isGlobal", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'isGlobal' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'isGlobal' is None", UserWarning)
        if getattr(self._obj, "shortLabel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'shortLabel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'shortLabel' is None", UserWarning)


    def build(self) -> ReferenceBase:
        """Build and return the ReferenceBase instance with validation."""
        self._validate_instance()
        return self._obj